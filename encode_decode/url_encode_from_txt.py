
from urllib import parse
from urllib import request

"""
python 3.x

从txt读取文件，然后进行转换

"""

#txt文件放到同一个目录下
#读文件
def read_from_txt(filename):
    datalist=[]  #保存所有的job
    with open(filename,encoding='UTF-8') as fr:    
        lines2=fr.readlines()
        lines=[]
        for line in lines2:
            #去掉空行
            if line=='\n':
                line=line.strip('\n')
            else:
                lines.append(line)
       
        for line in lines:         
            listdatas=line.strip().split(',') #去除空白和逗号“,”分割
            print('line-----',line)
            #print('len(listdatas)',len(listdatas))         
           
            datalist.append(listdatas)
            #print(datalist)                          
    return datalist

#写入文件，最多N条进行拆分
def write_to_txt(datas,maxnum=0,name="_result.txt"):
    #为0为不拆分数据
    if maxnum==0:
        j=0
        filename="write"+name
        with open(filename,'w+') as fw:
            for line in datas:
                fw.writelines(line)
                fw.write('\n')
                j+=1
                print('--------------',line,j)
    else:
        #拆分文件数
        num=1       
        for i in len(datas):
            j=0
            while j>maxnum:
                j=0               
                num=num+1                   
                filename="write"+"{}_{}.txt".format(name.split('.')[0],num)
            
            with open(filename,'w') as fw:
                fw.write(line[i])
                j+=1
        
#编码    
def data_encode(datas,type=0): 
    #0为字符串,1为list
    datalist=[]
    if type==0:
        strEncode = parse.quote(datas) #解码字符串
        print('字符串进行编码 ',strEncode)              
        datalist.append(strEncode)

    elif type==1:
        strlist=[]
        for i in range(len(datas)):
            strList=str(datas[i])
            strEncode = parse.quote(strList) #解码字符串
            print('字符串进行编码 ',strEncode)
            datalist.append(strEncode)

    return datalist

#解码
def data_decode(datas,type=0):
    #0为字符串,1为list
    datalist=[]
    if type==0:            
        strDecode = parse.unquote(datas) #解码字符串
        print('字符串进行解码 ',strDecode)
        datalist.append(strDecode)

    elif type==1:
        strlist=[]
        for i in range(len(datas)):
            strList=str(datas[i])
            strlist.append(strList)
            strDecode = parse.unquote(strList) #解码字符串
            print('字符串进行解码 ',strDecode)
            datalist.append(strDecode)

        '''
        for s in strlist:
            strDecode = parse.unquote(s) #解码字符串
            print('字符串进行解码 ',strDecode)
            datalist.append(strDecode)
        '''          
    return datalist


def readTXTfile_Encode(filename):
    datas=read_from_txt(filename)
    #encode
    datas=data_encode(datas,type=1)
    write_to_txt(datas,name="_Encode.txt")
        
    
def readTXTfile_Decode(filename):
    datas=read_from_txt(filename)
    #encode
    datas=data_decode(datas,type=1)
    write_to_txt(datas,name="_Decode.txt")    



#s="https%3a%2f%2fblog.csdn.net%2fu013833031%2farticle%2fdetails%2f78828539%e4%b8%ad%e5%9b%bd%e6%96%87%26%e5%9c%b0%e5%9d%80%26token%3dadfasdf+asdfasd+fa+sd%242ddfdsfads3"
#data_decode(s,type=0)                          


filename="url.txt"
#Encode
readTXTfile_Encode(filename)

#Decode
filename="url_encode.txt"
readTXTfile_Decode(filename)


