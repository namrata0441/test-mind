
    DELETE FROM Answers;
    DELETE FROM Questions;
    DELETE FROM Categories;
    VACUUM; -- Reclaim space from deleted data

    -- Insert both desired Categories
    INSERT INTO Categories (CategoryName) VALUES ('COMP202 - Data Structures & Algorithms');
    INSERT INTO Categories (CategoryName) VALUES ('EEEG202 - Basic Electronics');



    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'Suppose the numbers 7, 3, 1, 8, 3, 0, 9, 3, 4, 2 are inserted in that order into an initially empty binary search tree. The number of nodes in the left sub-tree containing no duplicate numbers, and its in-order traversal sequence of the resultant tree?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Suppose the numbers 7, 3, 1, 8, 3, 0, 9, 3, 4, 2 are inserted in that order into an initially empty binary search tree. The number of nodes in the left sub-tree containing no duplicate numbers, and its in-order traversal sequence of the resultant tree?'), '0, 1, 2, 3, 4, 7, 8, 9', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Suppose the numbers 7, 3, 1, 8, 3, 0, 9, 3, 4, 2 are inserted in that order into an initially empty binary search tree. The number of nodes in the left sub-tree containing no duplicate numbers, and its in-order traversal sequence of the resultant tree?'), '3, 1, 0, 2, 4, 7, 8, 9', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Suppose the numbers 7, 3, 1, 8, 3, 0, 9, 3, 4, 2 are inserted in that order into an initially empty binary search tree. The number of nodes in the left sub-tree containing no duplicate numbers, and its in-order traversal sequence of the resultant tree?'), '7, 3, 1, 0, 2, 4, 8, 9', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Suppose the numbers 7, 3, 1, 8, 3, 0, 9, 3, 4, 2 are inserted in that order into an initially empty binary search tree. The number of nodes in the left sub-tree containing no duplicate numbers, and its in-order traversal sequence of the resultant tree?'), '0, 1, 2, 3, 4, 7, 9, 8', 0
    );

    -- Question 2 (COMP202): You are required to create a linked list for storing integer elements. Which of the following statements is TRUE about the amount of memory space?
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'You are required to create a linked list for storing integer elements. Which of the following statements is TRUE about the amount of memory space?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'You are required to create a linked list for storing integer elements. Which of the following statements is TRUE about the amount of memory space?'), 'Static linked list uses less memory than dynamic linked list.', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'You are required to create a linked list for storing integer elements. Which of the following statements is TRUE about the amount of memory space?'), 'Dynamic linked list uses less memory than static linked list.', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'You are required to create a linked list for storing integer elements. Which of the following statements is TRUE about the amount of memory space?'), 'Circular linked list uses more memory than dynamic linked list.', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'You are required to create a linked list for storing integer elements. Which of the following statements is TRUE about the amount of memory space?'), 'Single linked list uses more memory than circular linked list.', 0
    );

    -- Question 3 (COMP202): What is the sum of the following prefix expression? (+ * X Y Z + Y 42)
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'What is the sum of the following prefix expression? (+ * X Y Z + Y 42)'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the sum of the following prefix expression? (+ * X Y Z + Y 42)'), '(X * Y + Z) * (Y * 42)', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the sum of the following prefix expression? (+ * X Y Z + Y 42)'), 'X + (Y * Z) + Y + 42', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the sum of the following prefix expression? (+ * X Y Z + Y 42)'), 'X * Y * Z + Y * 42', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the sum of the following prefix expression? (+ * X Y Z + Y 42)'), '(X * Y + Z) + (Y + 42)', 1
    );

    -- Question 4 (COMP202): What is the time complexity of binary search algorithm?
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'What is the time complexity of binary search algorithm?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the time complexity of binary search algorithm?'), 'O(n)', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the time complexity of binary search algorithm?'), 'O(n log n)', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the time complexity of binary search algorithm?'), 'O(log n)', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the time complexity of binary search algorithm?'), 'O(1)', 0
    );

    -- Question 5 (COMP202): How many unlimited graphs (not necessarily connected) can be constructed out of a given set of ''n'' nodes? If ''n'' = 10?
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'How many unlimited graphs (not necessarily connected) can be constructed out of a given set of ''n'' nodes? If ''n'' = 10?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'How many unlimited graphs (not necessarily connected) can be constructed out of a given set of ''n'' nodes? If ''n'' = 10?'), 'n*(n-1)/2', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'How many unlimited graphs (not necessarily connected) can be constructed out of a given set of ''n'' nodes? If ''n'' = 10?'), '10^4', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'How many unlimited graphs (not necessarily connected) can be constructed out of a given set of ''n'' nodes? If ''n'' = 10?'), '2^10', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'How many unlimited graphs (not necessarily connected) can be constructed out of a given set of ''n'' nodes? If ''n'' = 10?'), '2^(n(n-1)/2)', 1
    );

    -- Question 6 (COMP202): What is the position of the middle element in a binary search, in an array with elements indexed from low to high?
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'What is the position of the middle element in a binary search, in an array with elements indexed from low to high?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the position of the middle element in a binary search, in an array with elements indexed from low to high?'), 'high + low', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the position of the middle element in a binary search, in an array with elements indexed from low to high?'), 'low + high - 1', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the position of the middle element in a binary search, in an array with elements indexed from low to high?'), '(low + high) / 2', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the position of the middle element in a binary search, in an array with elements indexed from low to high?'), 'low + high + 1 / 2', 0
    );

    -- Question 7 (COMP202): Which data structure uses LIFO principle?
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'Which data structure uses LIFO principle?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which data structure uses LIFO principle?'), 'Queue', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which data structure uses LIFO principle?'), 'Stack', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which data structure uses LIFO principle?'), 'Linked List', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which data structure uses LIFO principle?'), 'Tree', 0
    );


    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'If you push the values 1, 2, and 3 in that order onto a stack, and then Pop three times, in what order will the values be popped?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'If you push the values 1, 2, and 3 in that order onto a stack, and then Pop three times, in what order will the values be popped?'), '1, 2, 3', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'If you push the values 1, 2, and 3 in that order onto a stack, and then Pop three times, in what order will the values be popped?'), '3, 2, 1', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'If you push the values 1, 2, and 3 in that order onto a stack, and then Pop three times, in what order will the values be popped?'), '1, 3, 2', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'If you push the values 1, 2, and 3 in that order onto a stack, and then Pop three times, in what order will the values be popped?'), '2, 1, 3', 0
    );

 array that is very large and spread over several disk blocks.
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'Spread Spectrum algorithm is a how for finding an element in a sorted array that is very large and spread over several disk blocks.'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Spread Spectrum algorithm is a how for finding an element in a sorted array that is very large and spread over several disk blocks.'), 'Divide and conquer', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Spread Spectrum algorithm is a how for finding an element in a sorted array that is very large and spread over several disk blocks.'), 'Exponential search', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Spread Spectrum algorithm is a how for finding an element in a sorted array that is very large and spread over several disk blocks.'), 'Interpolation search', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Spread Spectrum algorithm is a how for finding an element in a sorted array that is very large and spread over several disk blocks.'), 'Linear search', 0
    );


    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'Which one is an important factor in hash function?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which one is an important factor in hash function?'), 'The ratio of number of elements to the number of slots.', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which one is an important factor in hash function?'), 'The ratio of slots to the number of elements.', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which one is an important factor in hash function?'), 'The ratio of keys to slots in the table', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which one is an important factor in hash function?'), 'The ratio of keys to values in the table', 0
    );


    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'Which data structure (list, queue, stack, tree) is often called (heap) in of ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which data structure (list, queue, stack, tree) is often called (heap) in of ________'), 'Binary Tree', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which data structure (list, queue, stack, tree) is often called (heap) in of ________'), 'Complete Binary Tree', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which data structure (list, queue, stack, tree) is often called (heap) in of ________'), 'Binary search tree', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which data structure (list, queue, stack, tree) is often called (heap) in of ________'), 'General purpose hash table', 0
    );


    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'What is the time complexity of searching for an element in a hash table with a good hash function and collision resolution?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the time complexity of searching for an element in a hash table with a good hash function and collision resolution?'), 'O(log n)', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the time complexity of searching for an element in a hash table with a good hash function and collision resolution?'), 'O(1)', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the time complexity of searching for an element in a hash table with a good hash function and collision resolution?'), 'O(n)', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the time complexity of searching for an element in a hash table with a good hash function and collision resolution?'), 'O(log n)', 0
    );


    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'Which of the following traversal method uses pre-order and post-order in the order left and right in the trees?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which of the following traversal method uses pre-order and post-order in the order left and right in the trees?'), 'Preorder Traversal', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which of the following traversal method uses pre-order and post-order in the order left and right in the trees?'), 'Postorder Traversal', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which of the following traversal method uses pre-order and post-order in the order left and right in the trees?'), 'Inorder Traversal', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which of the following traversal method uses pre-order and post-order in the order left and right in the trees?'), 'Level Order Traversal', 0
    );


    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'In a complete binary tree, how are nodes filled?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In a complete binary tree, how are nodes filled?'), 'All levels are not filled', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In a complete binary tree, how are nodes filled?'), 'All levels are fully filled', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In a complete binary tree, how are nodes filled?'), 'All levels except possibly the last are fully filled, and the last level is filled from left to right', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In a complete binary tree, how are nodes filled?'), 'The tree is filled from right to left', 0
    );


    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'What is the time complexity of searching an element in a balanced Binary Search Tree (BST)?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the time complexity of searching an element in a balanced Binary Search Tree (BST)?'), 'O(log n)', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the time complexity of searching an element in a balanced Binary Search Tree (BST)?'), 'O(n)', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the time complexity of searching an element in a balanced Binary Search Tree (BST)?'), 'O(n log n)', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the time complexity of searching an element in a balanced Binary Search Tree (BST)?'), 'O(n^2)', 0
    );


    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'For a linear search in an array of n elements, the best complexity for, best, worst and average cases are ________ respectively.'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'For a linear search in an array of n elements, the best complexity for, best, worst and average cases are ________ respectively.'), 'O(1), O(n) and O(n)', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'For a linear search in an array of n elements, the best complexity for, best, worst and average cases are ________ respectively.'), 'O(1), O(n log n) and O(n log n)', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'For a linear search in an array of n elements, the best complexity for, best, worst and average cases are ________ respectively.'), 'O(1), O(n) and O(n/2)', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'For a linear search in an array of n elements, the best complexity for, best, worst and average cases are ________ respectively.'), 'O(1), O(n) and O(n + 1)', 0
    );

    -- Question 17 (COMP202): What is the time complexity of Depth First Search (DFS) on a graph with VVV vertices and EEE edges?
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'What is the time complexity of Depth First Search (DFS) on a graph with VVV vertices and EEE edges?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the time complexity of Depth First Search (DFS) on a graph with VVV vertices and EEE edges?'), 'O(V * E)', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the time complexity of Depth First Search (DFS) on a graph with VVV vertices and EEE edges?'), 'O(V^2)', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the time complexity of Depth First Search (DFS) on a graph with VVV vertices and EEE edges?'), 'O(V+E)', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the time complexity of Depth First Search (DFS) on a graph with VVV vertices and EEE edges?'), 'O(V^2 * E)', 0
    );

    -- Question 18 (COMP202): What is the main advantage of using Insertion Sort on small or nearly sorted array?
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'What is the main advantage of using Insertion Sort on small or nearly sorted array?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the main advantage of using Insertion Sort on small or nearly sorted array?'), 'It can sort in O(n) time for nearly sorted arrays', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the main advantage of using Insertion Sort on small or nearly sorted array?'), 'It is an in-place sorting algorithm', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the main advantage of using Insertion Sort on small or nearly sorted array?'), 'It can sort in O(n log n) time for nearly sorted arrays', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the main advantage of using Insertion Sort on small or nearly sorted array?'), 'It is a stable sorting algorithm', 0
    );

    -- Question 19 (COMP202): The initial configuration of a queue is 'a, b, c, d' ('a' is in the front end). To get the configuration 'd, c, b, a' one needs minimum of ________
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'The initial configuration of a queue is ''a, b, c, d'' (''a'' is in the front end). To get the configuration ''d, c, b, a'' one needs minimum of ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The initial configuration of a queue is ''a, b, c, d'' (''a'' is in the front end). To get the configuration ''d, c, b, a'' one needs minimum of ________'), '2 additions and 2 deletions', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The initial configuration of a queue is ''a, b, c, d'' (''a'' is in the front end). To get the configuration ''d, c, b, a'' one needs minimum of ________'), '3 additions and 3 deletions', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The initial configuration of a queue is ''a, b, c, d'' (''a'' is in the front end). To get the configuration ''d, c, b, a'' one needs minimum of ________'), '4 additions and 3 deletions', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The initial configuration of a queue is ''a, b, c, d'' (''a'' is in the front end). To get the configuration ''d, c, b, a'' one needs minimum of ________'), '3 deletions and 4 insertions', 0
    );

    -- Question 20 (COMP202): What is the maximum number of nodes at level L (root is at level 0) in a binary tree?
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'COMP202 - Data Structures & Algorithms'),
        'What is the maximum number of nodes at level L (root is at level 0) in a binary tree?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the maximum number of nodes at level L (root is at level 0) in a binary tree?'), '2^L', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the maximum number of nodes at level L (root is at level 0) in a binary tree?'), '2^(L+1) - 1', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the maximum number of nodes at level L (root is at level 0) in a binary tree?'), 'L+1', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the maximum number of nodes at level L (root is at level 0) in a binary tree?'), '2L', 0
    );


    -- ===============================================
    -- Questions for 'EEEG202 - Basic Electronics' (Total: 20 questions)
    -- ===============================================

    -- Question 1 (EEEG202): P-N junction diode is used for ________
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'P-N junction diode is used for ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'P-N junction diode is used for ________'), 'regulator IC', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'P-N junction diode is used for ________'), 'amplifier', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'P-N junction diode is used for ________'), 'smoothing in circuit', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'P-N junction diode is used for ________'), 'rectifier circuit', 1
    );

    -- Question 2 (EEEG202): Addition of pentavalent impurity to a pure semiconductor creates many ________
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'Addition of pentavalent impurity to a pure semiconductor creates many ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Addition of pentavalent impurity to a pure semiconductor creates many ________'), 'free electrons', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Addition of pentavalent impurity to a pure semiconductor creates many ________'), 'valence electron', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Addition of pentavalent impurity to a pure semiconductor creates many ________'), 'holes', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Addition of pentavalent impurity to a pure semiconductor creates many ________'), 'bound holes', 0
    );

    -- Question 3 (EEEG202): Which of the following parameter will be very high in the CB configuration of a BJT?
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'Which of the following parameter will be very high in the CB configuration of a BJT?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which of the following parameter will be very high in the CB configuration of a BJT?'), 'current gain', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which of the following parameter will be very high in the CB configuration of a BJT?'), 'voltage gain', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which of the following parameter will be very high in the CB configuration of a BJT?'), 'input resistance', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which of the following parameter will be very high in the CB configuration of a BJT?'), 'output resistance', 1
    );

    -- Question 4 (EEEG202): The value of Rz required for an n-channel JFET with Vp = -10 V, Idss = 40 mA, and Vgs = -5V is ________
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'The value of Rz required for an n-channel JFET with Vp = -10 V, Idss = 40 mA, and Vgs = -5V is ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The value of Rz required for an n-channel JFET with Vp = -10 V, Idss = 40 mA, and Vgs = -5V is ________'), '750 Ω', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The value of Rz required for an n-channel JFET with Vp = -10 V, Idss = 40 mA, and Vgs = -5V is ________'), '1155 Ω', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The value of Rz required for an n-channel JFET with Vp = -10 V, Idss = 40 mA, and Vgs = -5V is ________'), '1500 Ω', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The value of Rz required for an n-channel JFET with Vp = -10 V, Idss = 40 mA, and Vgs = -5V is ________'), '1500 Ω', 0
    );

    -- Question 5 (EEEG202): The value of ripple factor in full wave rectifier circuit is nearly equal to ________
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'The value of ripple factor in full wave rectifier circuit is nearly equal to ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The value of ripple factor in full wave rectifier circuit is nearly equal to ________'), '1.05', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The value of ripple factor in full wave rectifier circuit is nearly equal to ________'), '0.82', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The value of ripple factor in full wave rectifier circuit is nearly equal to ________'), '1.21', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The value of ripple factor in full wave rectifier circuit is nearly equal to ________'), '1.11', 0
    );

    -- Question 6 (EEEG202): Which of the following is NOT a necessary component in a clamper circuit?
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'Which of the following is NOT a necessary component in a clamper circuit?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which of the following is NOT a necessary component in a clamper circuit?'), 'Resistor', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which of the following is NOT a necessary component in a clamper circuit?'), 'Diode', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which of the following is NOT a necessary component in a clamper circuit?'), 'DC supply', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'Which of the following is NOT a necessary component in a clamper circuit?'), 'Capacitor', 0
    );

    -- Question 7 (EEEG202): The input impedance of an transistor is ________
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'The input impedance of an transistor is ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The input impedance of an transistor is ________'), 'very low', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The input impedance of an transistor is ________'), 'high', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The input impedance of an transistor is ________'), 'almost zero', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The input impedance of an transistor is ________'), 'low', 1
    );

    -- Question 8 (EEEG202): The current amplification factor in CC configuration is ________
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'The current amplification factor in CC configuration is ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The current amplification factor in CC configuration is ________'), '1α', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The current amplification factor in CC configuration is ________'), '1γ', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The current amplification factor in CC configuration is ________'), '1β', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The current amplification factor in CC configuration is ________'), '1γ', 0
    );

    -- Question 9 (EEEG202): In BJT, the equation IC = αIe + ________
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'In BJT, the equation IC = αIe + ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In BJT, the equation IC = αIe + ________'), 'IEO', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In BJT, the equation IC = αIe + ________'), 'ICAO', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In BJT, the equation IC = αIe + ________'), 'ICBO', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In BJT, the equation IC = αIe + ________'), 'ICO', 0
    );

    -- Question 10 (EEEG202): In a transistor, IC = 100 mA and IE = 100.2 mA. The value of β is ________
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'In a transistor, IC = 100 mA and IE = 100.2 mA. The value of β is ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In a transistor, IC = 100 mA and IE = 100.2 mA. The value of β is ________'), '200', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In a transistor, IC = 100 mA and IE = 100.2 mA. The value of β is ________'), '500', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In a transistor, IC = 100 mA and IE = 100.2 mA. The value of β is ________'), '100', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In a transistor, IC = 100 mA and IE = 100.2 mA. The value of β is ________'), '150', 0
    );

    -- Question 11 (EEEG202): As the temperature of a transistor goes up, the base-emitter resistance ________
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'As the temperature of a transistor goes up, the base-emitter resistance ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'As the temperature of a transistor goes up, the base-emitter resistance ________'), 'decrease', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'As the temperature of a transistor goes up, the base-emitter resistance ________'), 'increase', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'As the temperature of a transistor goes up, the base-emitter resistance ________'), 'remains constant', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'As the temperature of a transistor goes up, the base-emitter resistance ________'), 'fluctuates', 0
    );

    -- Question 12 (EEEG202): NPN transistors are preferred over PNP transistors because they have ________
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'NPN transistors are preferred over PNP transistors because they have ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'NPN transistors are preferred over PNP transistors because they have ________'), 'high mobility of holes', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'NPN transistors are preferred over PNP transistors because they have ________'), 'high mobility of electrons', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'NPN transistors are preferred over PNP transistors because they have ________'), 'high mobility of electrons compares to holes', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'NPN transistors are preferred over PNP transistors because they have ________'), 'low mobility of holes', 0
    );

    -- Question 13 (EEEG202): The input/output relationship of CB amplifier is ________
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'The input/output relationship of CB amplifier is ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The input/output relationship of CB amplifier is ________'), '180-degree', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The input/output relationship of CB amplifier is ________'), '270-degree', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The input/output relationship of CB amplifier is ________'), '0-degree', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The input/output relationship of CB amplifier is ________'), '-180 degree', 0
    );

    -- Question 14 (EEEG202): What is the main function of a diode in a circuit?
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'What is the main function of a diode in a circuit?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the main function of a diode in a circuit?'), 'To amplify signals', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the main function of a diode in a circuit?'), 'To store charge', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the main function of a diode in a circuit?'), 'To allow current flow in one direction only', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'What is the main function of a diode in a circuit?'), 'To provide resistance', 0
    );

    -- Question 15 (EEEG202): The crossover distortion does not occur in ________
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'The crossover distortion does not occur in ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The crossover distortion does not occur in ________'), 'Class pull', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The crossover distortion does not occur in ________'), 'Class B', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The crossover distortion does not occur in ________'), 'Class AB', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The crossover distortion does not occur in ________'), 'Class A', 1
    );

    -- Question 16 (EEEG202): A power amplifier delivers 25W of ac power to a 4 ohm speaker load. If the dc input power is 40W, what is the efficiency of this amplifier?
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'A power amplifier delivers 25W of ac power to a 4 ohm speaker load. If the dc input power is 40W, what is the efficiency of this amplifier?'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'A power amplifier delivers 25W of ac power to a 4 ohm speaker load. If the dc input power is 40W, what is the efficiency of this amplifier?'), '62.5%', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'A power amplifier delivers 25W of ac power to a 4 ohm speaker load. If the dc input power is 40W, what is the efficiency of this amplifier?'), '178%', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'A power amplifier delivers 25W of ac power to a 4 ohm speaker load. If the dc input power is 40W, what is the efficiency of this amplifier?'), '25%', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'A power amplifier delivers 25W of ac power to a 4 ohm speaker load. If the dc input power is 40W, what is the efficiency of this amplifier?'), '125%', 0
    );

    -- Question 17 (EEEG202): In case of Class A amplifier, the efficiency can be increased by ________ times using transformer coupled output.
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'In case of Class A amplifier, the efficiency can be increased by ________ times using transformer coupled output.'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In case of Class A amplifier, the efficiency can be increased by ________ times using transformer coupled output.'), '1', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In case of Class A amplifier, the efficiency can be increased by ________ times using transformer coupled output.'), '2', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In case of Class A amplifier, the efficiency can be increased by ________ times using transformer coupled output.'), '1.5', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In case of Class A amplifier, the efficiency can be increased by ________ times using transformer coupled output.'), '1.1', 0
    );

    -- Question 18 (EEEG202): In Class B amplifier, the output current flows for ________
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'In Class B amplifier, the output current flows for ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In Class B amplifier, the output current flows for ________'), '90-degree', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In Class B amplifier, the output current flows for ________'), '180-degree', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In Class B amplifier, the output current flows for ________'), '270-degree', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'In Class B amplifier, the output current flows for ________'), '360-degree', 0
    );

    -- Question 19 (EEEG202): When a sine wave of 1 Volt peak amplitude is passed through an operational amplifier of 1V, V/micro second, it can be a ________
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'When a sine wave of 1 Volt peak amplitude is passed through an operational amplifier of 1V, V/micro second, it can be a ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'When a sine wave of 1 Volt peak amplitude is passed through an operational amplifier of 1V, V/micro second, it can be a ________'), 'cosine wave', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'When a sine wave of 1 Volt peak amplitude is passed through an operational amplifier of 1V, V/micro second, it can be a ________'), 'square wave', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'When a sine wave of 1 Volt peak amplitude is passed through an operational amplifier of 1V, V/micro second, it can be a ________'), 'random wave', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'When a sine wave of 1 Volt peak amplitude is passed through an operational amplifier of 1V, V/micro second, it can be a ________'), 'triangular wave', 0
    );

    -- Question 20 (EEEG202): The 'slew rate' of an operational amplifier indicates ________
    INSERT INTO Questions (CategoryID, QuestionText) VALUES (
        (SELECT CategoryID FROM Categories WHERE CategoryName = 'EEEG202 - Basic Electronics'),
        'The ''slew rate'' of an operational amplifier indicates ________'
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The ''slew rate'' of an operational amplifier indicates ________'), 'how fast its output voltage can be changed.', 1
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The ''slew rate'' of an operational amplifier indicates ________'), 'how fast its output impedance can be changed.', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The ''slew rate'' of an operational amplifier indicates ________'), 'how fast its input current can be changed.', 0
    );
    INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES (
        (SELECT QuestionID FROM Questions WHERE QuestionText = 'The ''slew rate'' of an operational amplifier indicates ________'), 'how fast its output voltage can be changed.', 0
    );
