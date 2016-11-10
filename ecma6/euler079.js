/**
 * A common security method used for online banking is to ask the user for three random characters from a passcode.
 * For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply
 * would be: 317.

 The text file, keylog.txt, contains fifty successful login attempts.

 Given that the three characters are always asked for in order, analyse the file so as to determine the shortest
 possible secret passcode of unknown length.

 * Created by gcharles on 10/15/16.
 */
var euler079 = function () {
    class Graph {
        constructor(keys) {
            this.nodes = new Map();
            this.nodeCount = 0;

            keys.forEach(key => {
                let digits = key.split('');
                for (let i = 0; i < digits.length; ++i) {
                    this.addNode(digits[i]);
                    for (let j = 0; j < i; ++j) {
                        this.addEdge(digits[j], digits[i]);
                    }
                }
            });
        }

        addNode(node) {
            if (!this.nodes.get(node)) {
                ++this.nodeCount;
                this.nodes.set(node, new Set());
            }
        }

        removeNode(node) {
            this.nodes.delete(node);
            --this.nodeCount;
            for (let valueSet of this.nodes.values()) {
                valueSet.delete(node);
            }
        }

        addEdge(from, to) {
            this.nodes.get(to).add(from);
        }

        isEmpty() {
            return this.nodeCount == 0;
        }

        getNext() {
            for (let entry of this.nodes.entries()) {
                if (entry[1].size === 0) {
                    return entry[0];
                }
            }
            return null;
        }

    }

    return new EulerProblem({
        problem: 79,
        testInput: null,
        realInput: 'p079_keylog.txt',
        realOutput: 73162890,

        solver: function(filePath) {

            let result = '';
            let text = readEulerDataFile(filePath);
            let keys = text.split('\n').filter(line => line.trim().length > 0).map(key => key.trim());
            let graph = new Graph(keys);

            while (!graph.isEmpty()) {
                let next = graph.getNext();
                if (next === null) {
                    return 'cycle';
                } else {
                    graph.removeNode(next);
                    result += next;
                }
            }

            return parseInt(result);
        }
    });
}();
