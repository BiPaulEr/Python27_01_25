def try_syntax(numerator, denominator):
        print(f'In the try block: {numerator}/{denominator}')
        result = numerator / denominator
        return result
try :
    r = try_syntax(12, 4)
except ZeroDivisionError as ze:
      print({ze})
except Exception as e:
      print({e})
