from flask import Flask, render_template, request
import heapq

app = Flask(__name__)

graph = {
    "Shaheb Bazar": {
        "Talaimari": 3,
        "Laxmipur": 2
    },
    "Talaimari": {
        "Shaheb Bazar": 3,
        "Kazla": 2
    },
    "Laxmipur": {
        "Shaheb Bazar": 2,
        "Rail Gate": 3
    },
    "Rail Gate": {
        "Laxmipur": 3,
        "Kazla": 2
    },
    "Kazla": {
        "Rail Gate": 2,
        "Talaimari": 2,
        "Rajshahi University": 2
    },
    "Rajshahi University": {
        "Kazla": 2,
        "Court Station": 4
    },
    "Court Station": {
        "Rajshahi University": 4
    }
}

def dijkstra(graph, start, end):
    pq = [(0, start, [])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        path = path + [node]

        if node == end:
            return cost, path

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (cost + weight, neighbor, path)
                )

    return float('inf'), []

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        source = request.form["source"]
        destination = request.form["destination"]

        distance, path = dijkstra(
            graph,
            source,
            destination
        )

        result = {
            "distance": distance,
            "path": " → ".join(path)
        }

    locations = list(graph.keys())

    return render_template(
        "index.html",
        locations=locations,
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)