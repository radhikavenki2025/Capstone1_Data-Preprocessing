def QuanQual(st_habits1):
    quan=[]
    qual=[]
    for columnname in st_habits1.columns:
        print(columnname)
        if(st_habits1[columnname].dtype=='O'):
            qual.append(columnname)
        else:
            quan.append(columnname)
    return quan,qual
