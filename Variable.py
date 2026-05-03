import orderbook_wrapper as lib
import streamlit as st

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
        engine = lib.Matching_Engine()
        agents = lib.Agents()

        whale_agent = agents.whale(market)
        market_maker = agents.market_maker(market)
        noise_trader = agents.noise_trader(market)
        trend_follower = agents.trend_follower(market)

        while(self.simulation == True):
            for i in range(1, self.whale):
                whale_agent.execute_agent()
                engine.checker()

            for i in range(1, self.market_maker):
                market_maker.execute_agent()
                engine.checker()
    
            for i in range(1, self.noise_trader):
                noise_trader.execute_agent()
                engine.checker()

            for i in range(1, self.trend_follower):
                trend_follower.execute_agent()
                engine.checker()
    
    def print_book(self):
        if(self.simulation == True):
            m = lib.Global_Variables()

            if m.sellMap.empty() and m.buyMap.empty():
                st.text("")
            
            st.title("Order Book")

            for [price, level] in m.sellMap:
                total_shares = 0

                for order in level.orders:
                    total_shares += order.shares

                if total_shares > 0:
                    st.text(f"SELL:   $ {price} | {total_shares}")
                

            st.text("--------------------------------------")

            for [price, level] in m.buyMap:
                total_shares = 0

                for order in level.orders:
                    total_shares += order.shares


                if total_shares > 0:
                    st.text(f"BUY:   $ {price} | {total_shares}")