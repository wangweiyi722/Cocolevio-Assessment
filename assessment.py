# Make a company class to take in name,amount and price
class Company:
    
    def __init__(self, name, amount,price):
        self.name = name
        self.amount = amount
        self.price = price
        self.unitPrice = price/amount
        
    def __str__(self):
        
        return ("Name: " + self.name + ", " + "Units: " + str(self.amount) + ", " + "Price: " + str(self.price))

    

# Merge Sort Algorithm has a complexity of order nlog(n)
# In this case the list has to be a list of companies
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        mergeSort(lefthalf)
        mergeSort(righthalf)
        
        i = 0
        j = 0
        k = 0
        
        while i<len(lefthalf) and j<len(righthalf):
            
            # Sort the companies based on the price per unit sold
            if lefthalf[i].unitPrice < righthalf[j].unitPrice:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


def main():
    in_file = open('pricedata.csv','r')
    header = in_file.readline()
    print(header)
    companyList = []
    for line in in_file:
        values = line.rstrip().split(sep = ',')
        tempCompany = Company(values[0], int(values[1]), int(values[2]))
        companyList.append(tempCompany)

    mergeSort(companyList)
    for i in companyList:
        print(i.unitPrice)
    
    # This is the total number of units available for sale
    availUnits = int(input("Enter the number of units in stock: "))
    print()
    
    soldUnits = 0
    
    idx = len(companyList)-1
    
    # tracker keeps track of the companies that should be bought from
    tracker = []
    while idx >= 0 and soldUnits < availUnits:
        
        if soldUnits + companyList[idx].amount<=availUnits:
            tracker.append(companyList[idx])
            soldUnits += companyList[idx].amount
        
        idx -= 1
    
    for comp in tracker:
        print (comp)
    
main()