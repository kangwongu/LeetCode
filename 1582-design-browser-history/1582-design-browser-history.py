class Node:
    def __init__(self, url='', next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    # 초기화
    def __init__(self, homepage: str):
        self.head = self.current = Node(homepage)
        
    # 페이지 방문, 후의 기록을 지움
    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.current.next = new_node
        new_node.prev = self.current
        self.current = self.current.next
        
    # 뒤로 이동, 현재 위치 반환
    def back(self, steps: int) -> str:
        while self.current.prev is not None and steps > 0:
            steps -= 1
            self.current = self.current.prev
        return self.current.url
        
    # 앞으로 이동, 현재 위치 반환
    def forward(self, steps: int) -> str:
        while self.current.next is not None and steps > 0:
            steps -= 1
            self.current = self.current.next
        return self.current.url