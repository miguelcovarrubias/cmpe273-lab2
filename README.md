# CMPE-273 Lab-2

## By Miguel Covarrubias

### To build run:
``` 1. python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./calculator.proto```
``` 2. python calculator_server.py ```
``` 3. python calculator_clien.py ``` (In a separate teminal window)