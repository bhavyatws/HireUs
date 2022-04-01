

task=[  
    {'task1':'task1',
    'seniors':8,
    'juniors':0
    },
    {'task2':'task2',
        'seniors':8,
        'juniors':14
    },
    {   'task3':'task3',
        'seniors':6,
        'juniors':16
    },
    {   'task4':'task4',
        'seniors':5,
        'juniors':12
    },
     {   'task5':'task5',
        'seniors':6,
        'juniors':0
    },
    {   'task6':'task6',
        'seniors':8,
        'juniors':18
    },
    {   'task7':'task7',
        'seniors':9,
        'juniors':24
    },
    {   'task8':'task8',
        'seniors':2,
        'juniors':0
    },
    {   'task9':'task9',
        'seniors':4,
        'juniors':10
    },
    {   'task10':'task10',
        'seniors':6,
        'juniors':24
    },
   
]
total=0
total_hours_juniors=0
total_hours_seniors=0
task_seniors_only=[]
task_available_juniors=[]

#ratio=[10,20,30,40]
ratio=10

for tsk in task:
    
    total_hours_juniors=total_hours_juniors+tsk['juniors']
    total_hours_seniors=total_hours_seniors+tsk['seniors']
    if tsk['juniors']==0:
        task_seniors_only.append(tsk)
    else:
        task_available_juniors.append(tsk)
    
#function calculating ratio


# percentage=(total_hours_seniors/100)*ratio
# print(percentage)

# if percentage<=6.2:
#     pass
# elif(percentage<=12.4):
#     pass
    
# elif(percentage<=18.6):
#     pass
# elif(percentage<=24.8):
#     pass

# else:
#     print("Incorrect Ratio")
print("*********************************\n")
print("Total Hour(Juniors):",total_hours_juniors)

print("Total Hour(Seniors):",total_hours_seniors)
# print("Task seniors only",task_seniors_only)
# print("Task Available for juniors only",task_available_juniors)
total_task={}
assigned_task_juniors=[]

while(True):
    
    
    # n=int(input("Enter task: 0-9"))
    ratio=int(input("Enter ratio of senior you want to achieve:"))
    for n in range(10):
        print(n)
        
        total_hours_task_juniors=0
        total_hours_remaing_for_seniors=total_hours_seniors-task[n]['seniors']
        print("Total hours remaining for seniors:",total_hours_remaing_for_seniors)
        total_hours_task_juniors=total_hours_task_juniors+task[n]['juniors']
        print("Hours alloted for juniors:",total_hours_task_juniors)
        total=round(total_hours_remaing_for_seniors+total_hours_task_juniors)
        total_time="Total Time:"+''+ str(total)
        
        print("Total time:",total)
        calculated_ratio=round((total_hours_remaing_for_seniors/(total))*100)
        print("Ratio Senior",calculated_ratio)

        if round(calculated_ratio)==ratio:
            print("Your ratio matched")
            assigned_task_juniors.append(total_time)
            total_task['assigned_task_junior']=task[n]
            assigned_task_juniors.append(total_task)
            break

        if task[n] not in assigned_task_juniors:
            assigned_task_juniors.append(task[n])
        # print(task[n])
        # if task[n]['tas'] not in total_task['assigned_task_seniors']:
        #     total_task['assigned_task_seniors']=task[n]
        #     assigned_task_juniors.append(total_task)
            
             
    
    repeat=input("N or  n to exit")
    if repeat in "Nn":
        break 
print(assigned_task_juniors)
# django-insecure-nw93-^vr_5@8047+b%peuy_$#5b%5h*b38_a1rkc+((m3r3#q+
        

    



