class Solution(object):
    def maximumWealth(self, accounts):
        #
        max_wealth = 0 
        for customer in accounts :
            current_customer = sum(customer)
            if current_customer > max_wealth :
                max_wealth = current_customer
        return max_wealth
