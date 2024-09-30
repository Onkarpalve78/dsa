
print("Brute===>")


class StockSpanBruty():
    def __init__(self):
        self.stocks = []

    def stockSpannerBrute(self, n) -> int:
        if not n:
            return None
        self.stocks.append(n)
        consecutive_days_count = 0

        pointer = len(self.stocks)-1

        while pointer >= 0:
            if self.stocks[pointer] <= n:
                consecutive_days_count += 1

            else:
                break
            pointer -= 1
        print(consecutive_days_count)
        return consecutive_days_count


stockSpan = StockSpanBruty()

stockSpan.stockSpannerBrute(100)
stockSpan.stockSpannerBrute(80)
stockSpan.stockSpannerBrute(60)
stockSpan.stockSpannerBrute(70)
stockSpan.stockSpannerBrute([])
stockSpan.stockSpannerBrute(76)
stockSpan.stockSpannerBrute(86)
stockSpan.stockSpannerBrute(2)

print("Optimal===>")


class StockSpan():
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            value, last_span = self.stack.pop()

            span += last_span

        self.stack.append((price, span))
        print(span)
        return span


stockSpanMonotonicStack = StockSpan()

stockSpanMonotonicStack.next(1)
stockSpanMonotonicStack.next(2)
stockSpanMonotonicStack.next(4)
stockSpanMonotonicStack.next(2)
stockSpanMonotonicStack.next(7)
