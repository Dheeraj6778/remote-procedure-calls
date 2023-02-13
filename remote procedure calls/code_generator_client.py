import json
import sys
# generate rpc_client.py file
file=sys.argv[1]
f=open(file,'r')
st=""
for line in f.readlines():
    st+=line
json_obj=json.loads(st)
lst=json_obj["remote_procedures"]
code='import socket\n'
for x in lst:
    procedure_name = x['procedure_name']
    params=x['parameters']
    params_list=[]
    for param in params:
        params_list.append(param['parameter_name'])
    #print(params_list)
    param_string=procedure_name+"("+','.join(params_list)+')'
    params_list_temp=[]
    for x in params_list:
        st='{'+x+'}'
        params_list_temp.append(st)
    
    temp_str=' '.join(params_list_temp)
    #print(temp_str)
    code += f'def {param_string}:\n'
    code += '   clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n'
    code += '   host = socket.gethostname()\n'
    code += '   port = 9998\n'
    code += '   clientsocket.connect((host, port))\n'
    code += f'   message = f\'{procedure_name} {temp_str}\''+'\n'
    code += '   clientsocket.sendall(message.encode(\'utf-8\'))\n'
    code += '   data = clientsocket.recv(1024).decode(\'utf-8\')\n'
    code += '   clientsocket.close()\n'
    code += '   return data\n'

fp=open('rpc_client.py','w')
fp.write(code)
fp.close()


    
    
    

