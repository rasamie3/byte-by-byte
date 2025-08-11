import grpc

from concurrent import futures

import users_pb2
import users_pb2_grpc

class UserService(users_pb2_grpc.UsersServicer):

    def GetUsers(self, request, context):
        return  users_pb2.GetUsersResponse(
            user = [
                users_pb2.User(id="1", name="Rahma", email="irahmahussein@gmail.com"),
                users_pb2.User(id="2", name="Someonesname", email="someoneemail@gmail.com"),
            ]
        )
    
        
    def GetUserById(self, request, context):
        if request.id == "1":
            return users_pb2.GetUserByIdResponse(
                user=users_pb2.User(id="1", name="Rahma", email="irahmahussein@gmail.com")
            )
        return users_pb2.GetUserByIdResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UsersServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:8080")
    server.start()
    print("Server started on port 8080...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()