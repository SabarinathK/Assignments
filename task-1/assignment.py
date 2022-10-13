from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('calculator.html')


@app.route('/', methods=['POST'])
def result():
    try:
        operation_1 = request.form.get("operation_1", type=int, default=0)
        operation_2 = request.form.get("operation_2", type=int, default=0)
        operation = request.form.get("operation")
        if(operation == 'Addition'):
            result = operation_1 + operation_2 ,'Operation is Addition'
        elif(operation == 'Subtraction'):
            result = operation_1 - operation_2,'Operation is Subtraction'
        elif(operation == 'Multiplication'):
            result = operation_1 * operation_2,'Operation is Multiplication'
        elif(operation == 'Division'):
            if(operation_1==0 and operation_2==0):
                result = 0
            elif (operation_2==0):
                result = 'Not Possible'
            else:
                result = operation_1 / operation_2,'Operation is Division'  
        else:
            result = 0
            
    except ZeroDivisionError:
        print ("ERROR: Caught division by zero!")
    except ValueError:
       print ("ERROR: Input number could not be parsed!")
    except OverflowError:
       print( "ERROR: Result too large! Overflow encountered")
   
    result = result
    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)