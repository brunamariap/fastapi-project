from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.trainers import ProfileTrainersReq
from domain.data.sqlalchemy_models import Profile_Trainers

from cqrs.trainers.command.create_handlers import AddTrainerCommandHandler
from cqrs.trainers.command.update_handlers import UpdateTrainerCommandHandler
from cqrs.trainers.command.delete_handlers import DeleteTrainerCommandHandler
from cqrs.commands import ProfileTrainerCommand
from cqrs.trainers.query.query_handlers import ListTrainerQueryHandler, ProfileTrainerListQuery, GetTrainerQueryHandler

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
    trainer = Profile_Trainers(firstname=req.firstname, lastname=req.lastname, age=req.age, position=req.position, tenure=req.tenure, shift=req.shift, id=req.id)
    command = ProfileTrainerCommand()
    command.details = trainer
    result = handler.handle(command)

    if result == True:
        return req
    else:
        return JSONResponse(content={"messgage": "create trainer problem encountere"}, status_code=500)


@router.get("/trainers/list")
def list_trainers(sess: Session = Depends(sess_db)):
    handler = ListTrainerQueryHandler(sess)
    query: ProfileTrainerListQuery = handler.handle()
    return query.records


@router.patch("/trainers/update")
def update_trainer(id: int, req: ProfileTrainersReq, sess: Session = Depends(sess_db)):
    trainer_dict = req.dict(exclude_unset=True)
    handler = UpdateTrainerCommandHandler(sess)
    command = ProfileTrainerCommand()
    command.details = trainer_dict
    result = handler.handle(id, command)

    if result:
        return JSONResponse(content={'message': 'trainer updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update trainer error'}, status_code=500)


@router.delete("/trainers/delete/{id}")
def delete_trainer(id: int, sess: Session = Depends(sess_db)):
    handler = DeleteTrainerCommandHandler(sess)
    result = handler.handle(id)
    if result:
        return JSONResponse(content={'message': 'trainer deleted successfully'}, status_code=200)
    else:
        return JSONResponse(content={'message': 'delete trainer error'}, status_code=500)


@router.get("/trainers/list/{id}", response_model=ProfileTrainersReq)
def get_trainer(id: int, sess: Session = Depends(sess_db)):
    handler = GetTrainerQueryHandler(sess, id)
    query: ProfileTrainerListQuery = handler.handle()
    return query.records