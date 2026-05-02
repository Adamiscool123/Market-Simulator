import orderbook_wrapper as lib

class Variables:
    def __init__(self):
        self.agg = 0
        self.whale = 0
        self.market_maker = 0
        self.noise_trader = 0
        self.trend_follower = 0
        self.simulation = False
    
    def run_simulation(self):
        if(self.simulation == False):
            return 0

        market = lib.GlobalVariables()
        book = lib.Order_Book()
        engine = lib.Matching_Engine()

        whale_agent = lib.whale(market)
        market_maker = lib.market_maker(market)
        noise_trader = lib.noise_trader(market)
        trend_follower = lib.trend_follower(market)

        while(self.simulation == True):
            for i in range(1, self.whale):
                whale_agent.execute_agent()
            




