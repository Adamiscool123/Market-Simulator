import orderbook_wrapper as lib
import streamlit as st

class Variables:
    def __init__(self):
        self.agg = 0
        self.whale = 0
        self.market_maker = 0
        self.noise_trader = 0
        self.trend_follower = 0
        self.variable = 0
        self.simulation = False
    
    def run_simulation(self, market):
        
        if(self.simulation == False):
            return 0

        self.variable = market
        engine = lib.Matching_Engine()

        whale_agent = lib.Whale(market)
        market_maker = lib.MarketMaker(market)
        noise_trader = lib.NoiseTrader(market)
        trend_follower = lib.TrendFollower(market)

        for i in range(self.whale):
            whale_agent.execute_agent()
            engine.checker(market)

        for i in range(self.market_maker):
            market_maker.execute_agent()
            engine.checker(market)

        for i in range(self.noise_trader):
            noise_trader.execute_agent()
            engine.checker(market)

        for i in range(self.trend_follower):
            trend_follower.execute_agent()
            engine.checker(market)
    
    def print_book(self):
        if self.simulation == False:
            st.warning("Simulation is not running.")
            return
        
        st.write("Sell levels:", list(m.sellMap.keys()))
        st.write("Buy levels:", list(m.buyMap.keys()))
        st.write("Price history length:", len(m.price_history))
        st.write("Last prices:", m.price_history[-10:])

        m = self.variable

        if m == 0:
            st.warning("No market data yet.")
            return

        if not m.sellMap and not m.buyMap:
            st.info("Order book is empty.")
            return

        st.title("Order Book")

        for price, level in m.sellMap.items():
            total_shares = 0

            for order in level.orders:
                total_shares += order.shares

            if total_shares > 0:
                st.text(f"SELL:   $ {price} | {total_shares}")

        st.text("--------------------------------------")

        for price, level in m.buyMap.items():
            total_shares = 0

            for order in level.orders:
                total_shares += order.shares

            if total_shares > 0:
                st.text(f"BUY:   $ {price} | {total_shares}")