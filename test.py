
import json



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
senior_task=[]
junior_task=[]
total_hours_seniors=0
total_hours_juniors=0


for tsk in task:

    total_hours_juniors=total_hours_juniors+tsk['juniors']
    total_hours_seniors=total_hours_seniors+tsk['seniors']
    if tsk['juniors']==0:
        senior_task.append(tsk)
    else:
        junior_task.append(tsk)

print(total_hours_juniors)
print(total_hours_seniors)
# print("Junior task",junior_task)

#sorting junior_task
sorted_junior_task=sorted(junior_task, key = lambda i: (i['juniors']))
print(sorted_junior_task)
copy_junior_task=sorted_junior_task.copy()

def calculating_senior_hours(senior_task):
    print("length",len(senior_task))
    total_senior_task_only=0
    for tsk in senior_task:
        
        total_senior_task_only=total_senior_task_only+tsk['seniors']
        # total_senior_task_only=total_hours_seniors
    # print(total_senior_task_only)
    return  total_senior_task_only

y=calculating_senior_hours(senior_task)
print(y)
def calculating_juniors_hours(sorted_junior_task):
    print("len junior",len(sorted_junior_task))
    total_junior_task_only=0
    for tsk in sorted_junior_task:
        
        total_junior_task_only=total_hours_juniors+tsk['juniors']
    # print(total_senior_task_only)
    return  total_junior_task_only
y=calculating_juniors_hours(sorted_junior_task)
print(y)

def calculation_ratio(senior_task,sorted_junior_task):
    total_senior_task_only=calculating_senior_hours(senior_task)
    total_junior_task_only=calculating_juniors_hours(sorted_junior_task)
    total=total_senior_task_only+total_junior_task_only
    
    calculated_ratio=round((total_senior_task_only/(total))*100)
    return calculated_ratio,total

calculated_ratio=calculation_ratio(senior_task,sorted_junior_task)
print(calculated_ratio)
# print("Total:",calculated_ratio)
in_ratio=int(input("Enter ratio you want senior:junior:"))


final_task={}
assigned_task=[]



if calculated_ratio[0]==in_ratio:
        final_task['total_time']=calculated_ratio[1]
        # print(final_task)
        final_task['senior_task']=senior_task
        final_task['junior_task']=sorted_junior_task
        assigned_task.append(final_task)
        # print(senior_task)
        print(calculated_ratio)

else:
    print(len(junior_task))
    print(f'junior_task={junior_task}')
    for n in range(len(sorted_junior_task)):
        
        # print("Tsk++++",tsk)
        if n not in range(len(senior_task)):
            senior_task.append( copy_junior_task[n])
            # sorted_junior_task.pop(n)
            
            

        print("Append",y)
        print(range(len(sorted_junior_task)))
        if n   in range(len(sorted_junior_task)):
           
            print("popping")
            sorted_junior_task.pop(n)
            print("After popping",sorted_junior_task)
        
        # calculating_senior_hours()
        # print(calculating_senior_hours)
        print(len(senior_task),len(sorted_junior_task))
        calculated_ratio=calculation_ratio(senior_task,sorted_junior_task)
        print("Calculated_Ratio:",calculated_ratio)
        if calculated_ratio[0]==in_ratio:
            final_task['total_time']=calculated_ratio[1]
            # print(final_task)
            final_task['senior_task']=senior_task
            final_task['junior_task']=sorted_junior_task
            assigned_task.append(final_task)
            # print(senior_task)
            print(calculated_ratio)
            # print(len(senior_task))
            break
        
# for tsk in junior_task:
#     print(tsk)
print(json.dumps(assigned_task,indent=4))

