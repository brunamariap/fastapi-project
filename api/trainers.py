from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.trainers import ProfileTrainersReq
from domain.data.sqlalchemy_models import Profile_Trainers
from repository.sqlalchemy.trainers import TrainerRepository
from typing import List

from cqrs.trainers.command.create_handlers import AddTrainerCommandHandler
from cqrs.commands import ProfileTrainerCommand
from cqrs.trainers.query.query_handlers import ListTrainerQueryHandler, ProfileTrainerListQuery

router = APIRouter()

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.post("/trainers/add")
def add_trainer(req: ProfileTrainersReq, sess: Session = Depends(sess_db)):
    handler = AddTrainerCommandHandler(sess)
    mem_profile = dict()
    mem_profile["id"] = req.id

    # repo: TrainerRepository = TrainerRepository(sess)
    trainer = Profile_Trainers(firstname=req.firstname, lastname=req.lastname, age=req.age, position=req.position, tenure=req.tenure, shift=req.shift, id=req.id)
    # res = repo.insert_trainer(trainer)
    # mem_profile["shift"] = req.shift
    print(trainer)
    command = ProfileTrainerCommand()
    command.details = trainer
    result = handler.handle(command)
    if result == True:
        return req
        # if result == True:
        #     return req
        # else:
        #     return JSONResponse(content={'message': "erro"}, status_code=500)
    # else:
    #     return JSONResponse(content={"messgage": "create trainer problem encountere"}, status_code=500)


@router.get("/trainers/list")
def list_trainers(sess: Session = Depends(sess_db)):
    handler = ListTrainerQueryHandler()
    query: ProfileTrainerListQuery = handler.handle()
    return query.records


@router.patch("/trainers/update")
def update_trainer(id: int, req: ProfileTrainersReq, sess: Session = Depends(sess_db)):
    pass


@router.delete("/trainers/delete/{id}")
def delete_trainer(id: int, sess: Session = Depends(sess_db)):
    pass


@router.get("/trainers/list/{id}", response_model=ProfileTrainersReq)
def get_trainer(id: int, sess: Session = Depends(sess_db)):
    pass