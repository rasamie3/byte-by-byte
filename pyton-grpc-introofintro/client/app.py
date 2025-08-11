import grpc
import users_pb2
import users_pb2_grpc

def run():
    with grpc.insecure_channel("server:8080") as channel:
        stub = users_pb2_grpc.UsersStub(channel)

        response = stub.GetUsers(users_pb2.GetUsersRequest())
        print("Users:")
        for user in response.users:
            print(f"{user.id}: {user.name} ({user.email})")

        response = stub.GetUserById(users_pb2.GetUserByIdRequest(id="1"))
        print("\nUser by ID:")
        print(f"{response.user.id}: {response.user.name} ({response.user.email})")

if __name__ == "__main__":
    run()