contract = [{'contno':'C12345','currency':'USD' }, {'contno':'B01234','currency':'HKD'}]
contract.sort(key= lambda item : item ['contno'] )
print(contract)
