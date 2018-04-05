# -*- coding: utf-8 -*-
"""
***** Calculator *****
"""
import datetime
import calculator

calculator.add(2,3)
calculator.subtract(10,3)
calculator.multiply(3,2)
calculator.divide(20,2)
calculator.modulo(15,4)

calculator.doCalc(0,2,2)
calculator.doCalc(1,2,2)
calculator.doCalc(2,2,2)

"""
***** Getting current session log: *****
"""
calculator.readLogFile()

"""
***** Getting logs from date: *****
"""

calculator.readLogsFromDate(datetime.date.today())
calculator.readLogsFromDate(datetime.date.today() - datetime.timedelta(days=1))