import time
import check_stock
file_test = open("log.txt", "w")

duration = 60*60*24*30
while (duration>0):
    check_stock.main()
    time.sleep(86400)
    duration = duration - 86400
    file_test.write(time.asctime())

file_test.close()