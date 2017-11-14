from django.http import HttpResponse
from django.db import connections
from django.conf import settings
from django.shortcuts import render
from .database import Database
import json
import datetime
def index(request):
    db = Database()
    db.connect()


    #load from json
    with open('C:\\Users\\Fox\\PycharmProjects\\bdlab2\\FruitsAndVegetablesSupply\\FAVS\\json_files\\fruits_and_vegetables.json','r') as f:
        tmp_str = f.read()
        fruits_and_vegetables = json.loads(tmp_str)
    with open('C:\\Users\\Fox\\PycharmProjects\\bdlab2\\FruitsAndVegetablesSupply\\FAVS\\json_files\\plantings.json','r') as f:
        tmp_str = f.read()
        plantings = json.loads(tmp_str)
    with open('C:\\Users\\Fox\\PycharmProjects\\bdlab2\\FruitsAndVegetablesSupply\\FAVS\\json_files\\storehouses.json','r') as f:
        tmp_str = f.read()
        storehouses = json.loads(tmp_str)
    with open('C:\\Users\\Fox\\PycharmProjects\\bdlab2\\FruitsAndVegetablesSupply\\FAVS\\json_files\\transport.json','r') as f:
        tmp_str = f.read()
        transport = json.loads(tmp_str)
    supply_to_storehouses = db.saveMainJson()

    #new wiev of supply (change id)
    new_supply = []
    for i in supply_to_storehouses:
        tmp =[]
        tmp.append(i[0])
        for j in fruits_and_vegetables:
            if j[0]== i[1]:
                tmp.append(str(j[1])+' '+ str(j[2]))
                break
        tmp.append(i[2])
        for j in plantings:
            if j[0] == i[3]:
                tmp.append(str(j[2]))
                break
        for j in storehouses:
            if j[0] == i[4]:
                tmp.append(str(j[1]))
                break
        date = ''
        for j in range(len(i[5])):
            if i[5][j]==',' or i[5][j]=='-':
                date = date + '-'
            else:
                date = date+i[5][j]
        tmp.append(date)
        for j in transport:
            if j[0] == i[6]:
                tmp.append(str(j[2]))
                break
        new_supply.append(tmp)
        tmp=[]

    if request.method == "POST":

        dictvalues = {}
        dictvalues['fruitsandvegetables']=[]
        for i in fruits_and_vegetables:
            dictvalues['fruitsandvegetables'].append((i[0], i[1]+' '+i[2]))
        dictvalues['plantings'] = []
        for i in plantings:
            dictvalues['plantings'].append((i[0], i[2]))
        dictvalues['storehouses'] = []
        for i in storehouses:
            dictvalues['storehouses'].append((i[0], i[1]))
        dictvalues['drivers'] = []
        for i in transport:
            dictvalues['drivers'].append((i[0], i[2]))

        if "c" in request.POST:
            for i in range(len(new_supply)):
                if new_supply[i][0] == int(request.POST['c']):
                    request.session['index'] = i
                    return render(request, 'FAVS/q.html', {'data': new_supply,'id':new_supply[i],'dictvalues':dictvalues})
        elif "applychange" in request.POST:
            indexl=request.session['index']
            new_supply[indexl][1] = request.POST['Фрукт/Овощ']
            new_supply[indexl][2] = int(request.POST['Количество'])
            new_supply[indexl][3] = request.POST['Посадка']
            new_supply[indexl][4] = request.POST['Склад']
            new_supply[indexl][5] = request.POST['Дата Поставки']
            new_supply[indexl][6] = request.POST['Водитель']

            new_tmp = new_supply[indexl].copy()
            for i in dictvalues["fruitsandvegetables"]:
                if i[1] == new_tmp[1]:
                    new_tmp[1] = i[0]
                    break
            for i in dictvalues["plantings"]:
                if i[1] == new_tmp[3]:
                    new_tmp[3] = i[0]
                    break
            for i in dictvalues["storehouses"]:
                if i[1] == new_tmp[4]:
                    new_tmp[4] = i[0]
                    break
            for i in dictvalues["drivers"]:
                if i[1] == new_tmp[6]:
                    new_tmp[6] = i[0]
                    break
            db.update(new_tmp)
            return render(request, 'FAVS/q.html', {'data': new_supply, 'id': None,'add':None})
        elif "d" in request.POST:
            num = 0
            for i in new_supply:
                num+=1
                if i[0] == int(request.POST['d']):
                    db.deletion(i)
                    del new_supply[num-1]
                    return render(request, 'FAVS/q.html', {'data': new_supply, 'id': None,'add':None})
        elif "insert" in request.POST:
            nextindex = new_supply[len(new_supply)-1][0]+1
            return render(request, 'FAVS/q.html', {'data': new_supply, 'id': None,'add':nextindex,'dictvalues':dictvalues})
        elif "applyinsert" in request.POST:
            tmp = []
            tmp.append(new_supply[len(new_supply)-1][0]+1)
            tmp.append(request.POST['Фрукт/Овощ'])
            tmp.append(request.POST['Количество'])
            tmp.append(request.POST['Посадка'])
            tmp.append(request.POST['Склад'])
            tmp.append(request.POST['Дата Поставки'])
            tmp.append(request.POST['Водитель'])
            new_supply.append(tmp)
            new_tmp = tmp.copy()
            for i in dictvalues["fruitsandvegetables"]:
                if i[1] == new_tmp[1]:
                    new_tmp[1] = i[0]
                    break
            for i in dictvalues["plantings"]:
                if i[1] == new_tmp[3]:
                    new_tmp[3] = i[0]
                    break
            for i in dictvalues["storehouses"]:
                if i[1] == new_tmp[4]:
                    new_tmp[4] = i[0]
                    break
            for i in dictvalues["drivers"]:
                if i[1] == new_tmp[6]:
                    new_tmp[6] = i[0]
                    break
            db.insert(new_tmp)
            return render(request, 'FAVS/q.html', {'data': new_supply, 'id': None,'add':None})
        else:
            return render(request, 'FAVS/q.html', {'data': new_supply, 'id': None,'add':None})
        return render(request, 'FAVS/q.html', {'data': new_supply, 'id': None, 'add': None})
    else:
        return render(request, 'FAVS/q.html', {'data': new_supply, 'id': None,'add':None})

def query(request):
    db = Database()
    db.connect()
    if "Query1" in request.POST:
        request.session['data1'] = request.POST['Дата От']
        data1=request.POST['Дата От']
        request.session['data2'] =request.POST['Дата До']
        data2=request.POST['Дата До']
        res=db.query1(data1, data2)
        return render(request, 'FAVS/Query.html',{'i':res,'data1':request.session['data1'],'data2':request.session['data2']})
    elif "Query2" in request.POST:
        request.session['number'] = request.POST['number']
        number = request.POST['number']
        res = db.query2(int(number))
        return render(request, 'FAVS/Query.html', {'i1': res,'number':request.session['number']})

    elif "Query3" in request.POST:
        request.session['word'] = request.POST['word']
        word = request.POST['word']
        res = db.query3(word)
        return render(request, 'FAVS/Query.html', {'i2': res,'word': request.session['word']})
    elif "Query4" in request.POST:
        request.session['text'] = request.POST['text']
        text = request.POST['text']
        res = db.query4(text)
        return render(request, 'FAVS/Query.html', {'i3': res,'text':request.session['text']})
    return render(request, 'FAVS/Query.html')
