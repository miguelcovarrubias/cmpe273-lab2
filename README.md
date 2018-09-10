# CMPE-273 Lab-2

This is a simple calculator that has a add function "add(x, y)" which uses gRPC server and a test client to invoke this addition service.  
## By Miguel Covarrubias

## To Run:

### 
``` 1. python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./calculator.proto```
###
``` 2. python calculator_server.py ```
###
``` 3. python calculator_clien.py ``` (In a separate teminal window)

### Sample Output
### To build run:
Input numbers 'a' and 'b' to calculate sum:  
a: 3.5  
b: 4.6  
Sum result: 8.1  
