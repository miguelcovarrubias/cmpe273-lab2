from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    print("Input numbers 'x' and 'y' to calculate sum:")
    x = float(input("x: "))
    y = float(input("y: "))
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.AddRequest(x=x, y=y))
    print("Sum result: " + str(response.result))


if __name__ == '__main__':
    run()
