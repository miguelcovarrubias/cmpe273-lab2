from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def run():
    print("Input numbers 'a' and 'b' to calculate sum:")
    a = float(input("a: "))
    b = float(input("b: "))
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.AddRequest(a=a, b=b))
    print("Sum result: " + str(response.result))


if __name__ == '__main__':
    run()
