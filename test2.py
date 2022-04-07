#Python Script to calculate ratio senior vs junior in terms of %

import json




task=[  
    {'task1':'task1',
    'seniors':8,
    'juniors':0
    },
    {'task2':'task2',
        'seniors':12,
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
#Custom round function which round 11,12,13,14 to 10
def custom_round(number):
    rounded = round(number/10)*10
    return rounded


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
sorted_junior_task=sorted(junior_task, key = lambda i: (i['juniors']),reverse=True)
print(sorted_junior_task)


def calculate_thrs_thjr():
    thrs=0
    thjr=0
    for tsk in senior_task:
        
        thrs=thrs+tsk['seniors']
    for tsk in sorted_junior_task:
        thjr=thjr+tsk['juniors']
    return thrs,thjr
thrs_thjr=calculate_thrs_thjr()
print("thrs,thjr",thrs_thjr)

def check_ratio(thrs,thjr):
    
    total=thrs+thjr
    print(total)
   
    calculated_ratio=(thrs/total)*100
    return calculated_ratio,total

y=(check_ratio(thrs_thjr[0],thrs_thjr[1]))

in_ratio=[10,20,30,40]






   
def hireus(in_ratio):
    final_task={}
    assigned_task=[]
    package={}
    # global assigned_task
    global thrs_thjr
    y=(check_ratio(thrs_thjr[0],thrs_thjr[1]))
    global sorted_junior_task
    if custom_round(y[0])==in_ratio:
            final_task['total_time']=y[1]
            final_task['ratio']=custom_round(y[0])
            final_task['senior_task']=senior_task
            final_task['junior_task']=sorted_junior_task
            assigned_task.append(final_task)
           

    else:
       
        for n in range(len(sorted_junior_task)):
            popped=sorted_junior_task.pop()
           
            senior_task.append(popped)
           
            thrs_thjr=calculate_thrs_thjr()
            
            y=(check_ratio(thrs_thjr[0],thrs_thjr[1]) )
            print("Total time:",y[1])
            print("Checking Ratio",custom_round(y[0]) )
            

        
            if custom_round(y[0])==in_ratio:
                final_task['ratio']=custom_round(y[0])
                final_task['total_time']=y[1]
                
                final_task['senior_task']=senior_task
               
               
                final_task['junior_task']=sorted_junior_task
               
                package['Package']=final_task
               
                assigned_task.append(package)
                break
 
    return assigned_task               
                
    
    
                
                
            

               
            
         
           
#final result
           
package_list=[]         
for i in in_ratio:  
    result=hireus(i)  
    
    package_list.append(result)
 

print(json.dumps(package_list,indent=4))