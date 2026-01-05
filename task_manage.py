class Task:
    def init(self, task_id, task_name, desc, status):
        self.tid = task_id
        self.tname = task_name
        self.desc = desc
        self.status = status
    
    def str(self):
        return f'Task ID : {self.tid}\nTask Name: {self.tname}\nDesc: {self.desc}\nStatus: {self.status}'
    
class ManageTask:
    def init(self):
        self.tasks = {}
    
    def addtask(self,task_id,task_name,desc,status):
        task = Task(task_id, task_name, desc, status)
        self.tasks[task_id] = task
        print('Task added successfully')
    def updatetask(self, task_id, task_name, desc, status):
        if task_id not in self.tasks:
            print('Task not found')
        else:
            task = self.tasks[task_id]
            task.tname = task_name
            task.desc = desc
            task.status = status
            print('Task updated successfully')
    def deletetask(self, task_id):
        if task_id not in self.tasks:
            print('Task not found')
        else:
            del self.tasks[task_id]
            print('Task deleted successfully')
    def viewtask(self,tid):
        if tid not in self.tasks:
            print('Task not found')
        else:
            print(self.tasks[tid])


manage = ManageTask()
c = True
while c == True:
    print('Select an operation\n1.Add Task\n2.Update Task\n3.Delete Task\n4.View Task\n5.Exit')
    ch = int(input("Enter a choice: "))
    if ch == 1:
        task_id = int(input('Enter Task id: '))
        task_name = input('Enter Task name: ')
        desc = input('Enter description: ')
        status = input('Enter status of the task: ')
        manage.addtask(task_id, task_name, desc, status)
    elif ch == 2:
        task_id = int(input('Enter the id of the task that you wish to update: '))
        task_name = input('Enter new Task name: ')
        desc = input('Enter new description: ')
        status = input('Enter status of the task: ')
        manage.updatetask(task_id, task_name, desc, status)
    elif ch == 3: 
        task_id = int(input('Enter the id of the task that you wish to delete: '))
        manage.deletetask(task_id)
    elif ch == 4:
        task_id = int(input('Enter the id of the task you want to display: '))
        manage.viewtask(task_id)
    elif ch == 5:
        c = False
    else: 
        print('Invalid Input')