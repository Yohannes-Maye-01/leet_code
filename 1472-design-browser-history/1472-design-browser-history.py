class BrowserHistory:
    def __init__(self, homepage: str):
        self.future = [] 
        self.current = 0 
        self.history = [homepage]
        

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current + 1] 
        self.history.append(url)
        self.current += 1
        self.future = [] 

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]

    