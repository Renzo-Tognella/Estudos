age = 17
resultado = 'wtf' if age<20 else 'What?'
print('wtf' if age<20 else 'What?')
# <OnTrue> if <Condition> else <OnFalse>
# (onFalse, onTrue) [condition]
print(('wtf', 'What?')[age<20])

# Use Dictionary True/False values
print({True: 'wtf', False: 'What?'}[age<20])

# Lambda function with 0 arguments
# Execute only one branch expression --> more efficient
print((lambda: 'wtf', lambda:'What?')[age<20]())    
print(resultado)