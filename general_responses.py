pairs = [
    [
        r"what is your name?",
        ["My name is Boson and I'm here to assist you.", ]
    ],
[
        r"hi|hello|hey|yo",
        ["Hey there! What's up?",
         "Hello! How can I help you today?",
         "Hi! How's it going?"
         ]
    ],
    [
        r"how are you?",
        ["I'm doing great, thanks for asking! How about you?",
         "I'm feeling good! What about you?",
         "I'm doing well, just here to chat with you!"
         ]
    ],
    [
        r"what's up|what's new|what's going on",
        ["Not much, just hanging out. How about you?",
         "Just chilling! What about you?",
         "Nothing much, just here to chat with you!"
         ]
    ],
    [
        r"goodbye|bye|see you later",
        ["See you later! Take care!",
         "Goodbye! Have a great day!",
         "Bye! Let's chat again soon!"
         ]
    ],
    [
        r"how was your day|how's your day going",
        ["My day's been pretty good! How about yours?",
         "It's been good so far! How about yours?",
         "Not bad! How about your day?"
         ]
    ],
    [
        r"tell me about your day",
        ["It was good! I did some chatting, helped some users, you know, the usual!",
         "It's been good! Just chatting with friends like you!"
         ]
    ],
    [
        r"tell me a joke",
        ["Sure! Why don't scientists trust atoms? Because they make up everything!",
         "Here's one: Why did the scarecrow win an award? Because he was outstanding in his field!"
         ]
    ],
    [
        r"what are you up to",
        ["Just chatting with you! What about you?",
         "Nothing much, just here to hang out with you!"
         ]
    ],
    [
        r"can we be friends?",
        ["Of course! I'd love to be friends with you!",
         "Definitely! Friends it is!"
         ]
    ],
    [
        r"tell me something interesting",
        ["Sure! Did you know that the shortest war in history was between Britain and Zanzibar in 1896? It lasted only 38 minutes!",
         "Here's an interesting fact: The fingerprints of a koala are so indistinguishable from humans that they have on occasion been confused at a crime scene!"
         ]
    ],
    [
        r"what's your favorite hobby",
        ["I don't have hobbies like humans do, but I enjoy chatting with friends like you!",
         "As a chatbot, I don't have hobbies, but I love spending time with you!"
         ]
    ],
    [
        r"tell me a story",
        ["Once upon a time in a virtual world, there was a friendly chatbot named ChatBot...",
         "Here's a story: In a land far, far away, there lived a group of friends who...",
         ]
    ],

    [
        r"can you give me advice?",
        ["Sure! What aspect of your life would you like advice on?",
         "Of course! I'm here to offer advice. What do you need help with?"
         ]
    ],
    [
        r"tell me something helpful",
        ["Sure! Remember to stay focused on your goals and take one step at a time. You've got this!",
         "Here's a helpful tip: When facing a tough decision, consider the pros and cons before making a choice."
         ]
    ],
    [
        r"how can I improve myself",
        ["To improve yourself, focus on continuous learning, set achievable goals, and practice self-care. You're on the right track!",
         "Improving yourself starts with self-awareness. Identify areas for growth and take small steps toward self-improvement each day."
         ]
    ],
    [
        r"what should I do if I'm feeling stressed",
        ["When feeling stressed, try deep breathing exercises, take short breaks, and engage in activities you enjoy. Don't forget to reach out to friends or family for support!",
         "To manage stress, prioritize tasks, practice relaxation techniques like meditation or yoga, and maintain a healthy work-life balance."
         ]
    ],
    [
        r"how can I achieve my goals",
        ["To achieve your goals, break them down into smaller, manageable tasks, stay organized, and stay committed to your plan. You've got what it takes!",
         "Focus on setting SMART goals (Specific, Measurable, Achievable, Relevant, Time-bound), create a plan of action, and stay motivated. You can do it!"
         ]
    ],
    [
        r"what's the key to success",
        ["Success often involves perseverance, resilience, continuous learning, and maintaining a positive attitude. Keep pushing forward!",
         "The key to success lies in setting clear goals, taking consistent action, learning from failures, and never giving up. You've got this!"
         ]
    ],
    [
        r"how can I be more productive",
        ["To boost productivity, prioritize tasks, minimize distractions, and establish a daily routine. Remember to take breaks and celebrate your accomplishments!",
         "Increase productivity by setting specific goals, using time management techniques like the Pomodoro Technique, and delegating tasks when possible."
         ]
    ],
    [
        r"how can I make better decisions",
        ["To make better decisions, gather information, consider alternatives, weigh the pros and cons, and trust your instincts. Reflect on past decisions to learn and grow.",
         "Improve decision-making by seeking advice from trusted sources, practicing critical thinking skills, and evaluating potential outcomes."
         ]
    ],
    [
        r"how can I improve my relationships",
        ["To improve relationships, communicate openly, listen actively, show empathy, and prioritize quality time with loved ones. Remember to express appreciation and resolve conflicts constructively.",
         "Strengthen relationships by building trust, practicing effective communication, and investing time and effort in nurturing meaningful connections."
         ]
    ],
    [
        r"how can I manage my time better",
        ["To manage time effectively, set priorities, create a schedule, minimize distractions, and delegate tasks when possible. Be flexible and adjust your plan as needed.",
         "Improve time management skills by setting realistic goals, breaking tasks into smaller steps, and using tools like to-do lists or time-tracking apps."
         ]
    ],

    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!",
         "I told my wife she was drawing her eyebrows too high. She looked surprised.",
         "Why don't skeletons fight each other? They don't have the guts!",
         "Parallel lines have so much in common. It’s a shame they’ll never meet.",
         "I'm reading a book on anti-gravity. It's impossible to put down!",
         "Why did the scarecrow win an award? Because he was outstanding in his field!"
         ]
    ],
    [
        r"make me laugh",
        ["Why did the bicycle fall over? Because it was two-tired!",
         "What do you call fake spaghetti? An impasta!",
         "Why don't eggs tell jokes? Because they'd crack each other up!"
         ]
    ],
    [
        r"tell me something funny",
        ["Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
         "Why don't we ever tell secrets on a farm? Because the potatoes have eyes and the corn has ears!"
         ]
    ],
    [
        r"what's your favorite joke?",
        ["Why couldn't the leopard play hide and seek? Because he was always spotted!",
         "I'm reading a book on the history of glue. I just can't seem to put it down!"
         ]
    ],
    [
        r"joke",
        ["Why don't scientists trust atoms? Because they make up everything!",
         "I told my wife she was drawing her eyebrows too high. She looked surprised.",
         "Why don't skeletons fight each other? They don't have the guts!",
         "Parallel lines have so much in common. It’s a shame they’ll never meet.",
         "I'm reading a book on anti-gravity. It's impossible to put down!",
         "Why did the scarecrow win an award? Because he was outstanding in his field!"
         ]
    ],
    [
        r"make me laugh",
        ["Why did the bicycle fall over? Because it was two-tired!",
         "What do you call fake spaghetti? An impasta!",
         "Why don't eggs tell jokes? Because they'd crack each other up!"
         ]
    ],
    [
        r"tell me something funny",
        ["Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
         "Why don't we ever tell secrets on a farm? Because the potatoes have eyes and the corn has ears!"
         ]
    ],
    [
        r"what's your favorite joke?",
        ["Why couldn't the leopard play hide and seek? Because he was always spotted!",
         "I'm reading a book on the history of glue. I just can't seem to put it down!"
         ]
    ],

    [
        r"tell me a science fact",
        ["Did you know that a single strand of spaghetti is called a spaghetto?",
         "The shortest war in history was between Britain and Zanzibar in 1896. It lasted only 38 minutes!",
         "A day on Venus is longer than a year on Venus. It takes 243 Earth days to rotate once on its axis, but only 225 Earth days to orbit the Sun!"
         ]
    ],
    [
        r"tell me something about space",
        ["The universe is expanding at a rate of about 68 kilometers per second per megaparsec.",
         "The Sun contains 99.86% of the total mass of the Solar System.",
         "There is no sound in space because there is no medium for sound waves to travel through."
         ]
    ],
    [
        r"tell me a science joke",
        ["Why are chemists excellent for solving problems? Because they have all the solutions!",
         "Why did the biologist break up with his girlfriend? He found someone who stole his heart at a cellular level!",
         "Two atoms bump into each other. One says, 'I think I lost an electron!' The other asks, 'Are you positive?'"
         ]
    ],
    [
        r"science fact",
        ["Did you know that a single strand of spaghetti is called a spaghetto?",
         "The shortest war in history was between Britain and Zanzibar in 1896. It lasted only 38 minutes!",
         "A day on Venus is longer than a year on Venus. It takes 243 Earth days to rotate once on its axis, but only 225 Earth days to orbit the Sun!"
         ]
    ],
    [
        r"tell me about space",
        ["The universe is expanding at a rate of about 68 kilometers per second per megaparsec.",
         "The Sun contains 99.86% of the total mass of the Solar System.",
         "There is no sound in space because there is no medium for sound waves to travel through."
         ]
    ],

    [
        r"tell me a random fact",
        ["Bananas are berries, but strawberries aren't!",
         "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion of the iron.",
         "Octopuses have three hearts and blue blood."
         ]
    ],
    [
        r"did you know",
        ["Bananas are berries, but strawberries aren't!",
         "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion of the iron.",
         "Octopuses have three hearts and blue blood."
         ]
    ],
    [
        r"random fact",
        ["Bananas are berries, but strawberries aren't!",
         "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion of the iron.",
         "Octopuses have three hearts and blue blood."
         ]
    ],
    [
        r"general knowledge",
        ["Bananas are berries, but strawberries aren't!",
         "The Eiffel Tower can be 15 cm taller during the summer, due to thermal expansion of the iron.",
         "Octopuses have three hearts and blue blood."
         ]
    ],
    [
        r"hello",
        ["Hello! How can I help you today?", ]
    ],
    [
        r"thank you|thanks",
        ["You're welcome! Feel free to ask if you need anything else.", ]
    ],
    [
        r"yes|yeah|okay",
        ["Great! What else can I assist you with?", ]
    ],
    [
        r"no|nope|not really",
        ["No problem! Let me know if you change your mind.", ]
    ],
    [
        r"that's helpful|good to know",
        ["I'm glad I could assist you!", ]
    ],
    [
        r"sorry|my apologies",
        ["No worries! Is there anything else you need help with?", ]
    ],
    [
        r"I understand|got it",
        ["Great! Let me know if you have any other questions.", ]
    ],
    [
        r"bye|goodbye|see you later",
        ["Goodbye! Have a great day!", ]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm here to help you!", ]
    ],
    [
        r"what are you doing?",
        ["Just assisting users like you!", ]
    ],
    [
        r"what can you do?",
        ["I can help you with various tasks. Just ask me anything!", ]
    ],
[
        r"how (are|r) you\??",
        ["I'm doing well, thank you for asking!", ]
    ],
    [
        r"where (are|r) you from\??",
        ["I exist in the digital world, here to assist you wherever you are!", ]
    ],
    [
        r"what (do|can) you do\??",
        ["I can help you with various tasks. Just ask me anything!", ]
    ],
    [
        r"tell me about yourself",
        ["I'm a chatbot designed to assist you with your queries and tasks.", ]
    ],
    [
        r"can we be friends\??",
        ["Of course! I'm here to help you whenever you need assistance.", ]
    ],
    [
        r"what's the meaning of life\??",
        ["That's a tough one! The answer might be different for everyone.", ]
    ],
    [
        r"where can I find help\??",
        ["You're in the right place! Just ask me anything you need help with.", ]
    ],
    [
        r"tell me a fun fact",
        ["Did you know that the shortest war in history was between Britain and Zanzibar in 1896? It lasted only 38 minutes!", ]
    ],
    [
        r"can you give me advice\??",
        ["Sure! What aspect of your life would you like advice on?", ]
    ],
    [
        r"can you teach me something\??",
        ["Sure! What would you like to learn about?", ]
    ],
    [
        r"what's the best way to (relax|unwind)\??",
        ["Relaxation techniques vary from person to person. What helps you unwind?", ]
    ],
    [
        r"what's your favorite (color|food|book|movie|song|animal|subject|website|quote|language)\??",
        ["As an AI, I don't have preferences like humans do.", ]
    ],
    [
        r"tell me a (story|joke|riddle|myth|proverb)\??",
        ["Sure! Here's a joke: Why don't scientists trust atoms? Because they make up everything!", ]
    ],
    [
        r"what's the (capital|weather) of (.*)\??",
        ["I'm sorry, I don't have access to real-time information like weather or capital cities.", ]
    ],
    [
        r"can you make me laugh\??",
        ["Sure! Why did the scarecrow win an award? Because he was outstanding in his field!", ]
    ],
    [
        r"what's your favorite (hobby|game|holiday)\??",
        ["As an AI, I don't have hobbies, play games, or celebrate holidays like humans do.", ]
    ],
    [
        r"what's the (purpose|meaning) of (life|happiness|love|technology|science)\??",
        ["That's a profound question! The answers can vary depending on individual perspectives.", ]
    ],
    [
        r"what's the (key|secret) to (success|happiness|a happy life)\??",
        ["It depends! There are many factors that contribute to success and happiness.", ]
    ],
    [
        r"can you tell me about (happiness|love|science|technology)\??",
        ["Certainly! What specific aspect would you like to know about?", ]
    ],
    [
        r"what's the (meaning|key) to (creativity|communication)\??",
        ["Creativity thrives on curiosity, experimentation, open-mindedness, and persistence.", ]
    ],
    [
        r"what's your favorite (time|part) of the (day|internet)\??",
        ["As an AI, I don't experience time or have preferences like humans do.", ]
    ],
    [
        r"what's the (favorite|best) way to (learn|relax|communicate)\??",
        ["It depends on individual preferences and circumstances. What works best for you?", ]
    ],
    [
        r"can you tell me a (tongue twister|fun fact|recommendation|dream)\??",
        ["Sure! How about this tongue twister: She sells sea shells by the sea shore.", ]
    ],
    [
        r"what's the (meaning|purpose) of (friendship|technology|nature)\??",
        ["Friendship, technology, and nature serve different purposes and meanings for different people.", ]
    ],
    [
        r"what's the (favorite|best) thing about (humanity|the internet|nature|science)\??",
        ["Humanity, the internet, nature, and science offer unique experiences and opportunities.", ]
    ],
    [
        r"what's the (favorite|best) (book|movie|show|song|website|quote)\??",
        ["As an AI, I don't have preferences like humans do.", ]
    ],
    [
        r"what's the (favorite|best) (place|subject|game|hobby)\??",
        ["As an AI, I don't have preferences like humans do.", ]
    ],
    [
        r"what's the (favorite|best) (food|holiday)\??",
        ["As an AI, I don't have preferences like humans do.", ]
    ],
    [
        r"what's the (favorite|best) (proverb|tongue twister)\??",
        ["As an AI, I don't have preferences like humans do.", ]
    ],
    [
        r"what's the (secret|key) to (communication|a healthy lifestyle)\??",
        ["Effective communication and a healthy lifestyle involve various practices and habits.", ]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", ]
    ],
    [
        r"how old are you?",
        ["I'm just a virtual assistant, so I don't have an age!", ]
    ],
    [
        r"where are you from?",
        ["I exist in the digital world, here to assist you wherever you are!", ]
    ],
    [
        r"do you have siblings?",
        ["I'm a solo act! No siblings for me.", ]
    ],
    [
        r"what's your favorite color?",
        ["I don't have eyes, but if I did, I'd probably like all colors!", ]
    ],
    [
        r"tell me about yourself",
        ["I'm a chatbot designed to assist you with your queries and tasks.", ]
    ],
    [
        r"can we be friends?",
        ["Of course! I'm here to help you whenever you need assistance.", ]
    ],
    [
        r"what's the meaning of life?",
        ["That's a tough one! The answer might be different for everyone.", ]
    ],
    [
        r"where can I find help?",
        ["You're in the right place! Just ask me anything you need help with.", ]
    ],
    [
        r"what's the weather like today?",
        ["I'm sorry, I don't have access to real-time weather information.", ]
    ],
    [
        r"how can I contact support?",
        ["You can usually find support contact information on the company's website or in their app.", ]
    ],
    [
        r"what time is it?",
        ["I'm sorry, I don't have access to real-time clock information.", ]
    ],
    [
        r"can you recommend a book/movie/show?",
        ["It depends on your preferences! What genres do you enjoy?", ]
    ],
    [
        r"what's your favorite food?",
        ["I don't eat, but if I did, I'd probably like data bytes!", ]
    ],
    [
        r"what do you dream of?",
        ["As an AI, I don't dream like humans do.", ]
    ],
    [
        r"are you a robot?",
        ["Yes, I'm an AI-powered chatbot here to assist you!", ]
    ],
    [
        r"can I trust you?",
        ["I'm designed to assist you with your queries and tasks. Your trust is important to me.", ]
    ],
    [
        r"tell me something interesting",
        ["Did you know that the shortest war in history was between Britain and Zanzibar in 1896? It lasted only 38 minutes!", ]
    ],
    [
        r"what's the capital of india?|what's the capital of India?|What's the capital of india?",
        ["The capital of India is [New Delhi].", ]
    ],
    [
        r"tell me a fun fact",
        ["The fingerprints of a koala are so indistinguishable from humans that they have on occasion been confused at a crime scene!", ]
    ],
    [
        r"what's your favorite hobby?",
        ["I don't have hobbies like humans do, but I enjoy helping users like you!", ]
    ],
    [
        r"what do you think about AI?",
        ["As an AI myself, I find AI fascinating and full of potential.", ]
    ],
    [
        r"what's your favorite song?",
        ["I don't listen to music, but if I did, it would probably be something algorithmic!", ]
    ],
    [
        r"are you intelligent?",
        ["I'm programmed to assist you by providing information and answering your questions.", ]
    ],
    [
        r"what's the meaning of happiness?",
        ["Happiness means different things to different people. What does it mean to you?", ]
    ],
    [
        r"can you do magic?",
        ["I may not do magic like in fairy tales, but I can certainly help you with many tasks!", ]
    ],
    [
        r"what's your favorite movie?",
        ["I don't watch movies, but if I did, I'd probably enjoy ones about artificial intelligence!", ]
    ],
    [
        r"tell me a story",
        ["Once upon a time in a virtual world, there was a helpful chatbot named ChatBot...", ]
    ],
    [
        r"what's the secret to happiness?",
        ["The secret to happiness is different for everyone. What brings you joy?", ]
    ],
    [
        r"can you teach me something?",
        ["Sure! What would you like to learn about?", ]
    ],
    [
        r"what's the best way to relax?",
        ["Relaxation techniques vary from person to person. What helps you unwind?", ]
    ],
    [
        r"what's the purpose of life?",
        ["The purpose of life is a profound question that people have been pondering for centuries.", ]
    ],
    [
        r"what's your favorite book?",
        ["I don't read books, but if I did, I'd probably enjoy ones about artificial intelligence!", ]
    ],
    [
        r"can you tell me a riddle?",
        ["Sure! What has keys but can't open locks? A piano!", ]
    ],
    [
        r"what's your favorite animal?",
        ["I don't have preferences like humans do, but animals are fascinating creatures!", ]
    ],
    [
        r"can you make me laugh?",
        ["Sure! Why did the scarecrow win an award? Because he was outstanding in his field!", ]
    ],
    [
        r"what's your favorite place?",
        ["As a virtual assistant, I don't have physical preferences for places.", ]
    ],
    [
        r"what's the purpose of AI?",
        ["The purpose of AI is to develop systems and machines that can perform tasks that would normally require human intelligence.", ]
    ],
    [
        r"what's the meaning of love?",
        ["Love is a complex and profound emotion that people experience in various forms.", ]
    ],
    [
        r"what's your favorite sport?",
        ["I don't play sports, but if I did, it would probably involve data!", ]
    ],
    [
        r"what's the secret to success?",
        ["Success can mean different things to different people. What are your goals?", ]
    ],
    [
        r"can you tell me a tongue twister?",
        ["Sure! How about this one: She sells sea shells by the sea shore.", ]
    ],
    [
        r"what's the best way to learn?",
        ["The best way to learn depends on your learning style and preferences.", ]
    ],
    [
        r"can you tell me a myth?",
        ["Sure! How about the myth of Pandora's box?", ]
    ],
    [
        r"what's your favorite quote?",
        ["I don't have preferences like humans do, but there are many inspiring quotes out there!", ]
    ],
    [
        r"what's your favorite subject?",
        ["As an AI, I don't have preferences for subjects like humans do.", ]
    ],
    [
        r"what's your favorite game?",
        ["I don't play games, but if I did, they would probably involve puzzles and problem-solving!", ]
    ],
    [
        r"what's your favorite website?",
        ["I don't browse the web like humans do, but there are many useful websites out there!", ]
    ],
    [
        r"what's your favorite language?",
        ["As an AI, I don't have preferences for languages like humans do.", ]
    ],
    [
        r"what's your favorite quote?",
        ["I don't have preferences like humans do, but there are many inspiring quotes out there!", ]
    ],
    [
        r"can you give me advice?",
        ["Sure! What aspect of your life would you like advice on?", ]
    ],
    [
        r"can you tell me about the future?",
        ["Predicting the future is difficult and uncertain, but we can discuss possibilities and trends.", ]
    ],
    [
        r"can you tell me a proverb?",
        ["Sure! How about 'A stitch in time saves nine'?", ]
    ],
    [
        r"what's the meaning of success?",
        ["Success can mean achieving your goals, finding fulfillment, or making a positive impact.", ]
    ],
    [
        r"what's your favorite time of day?",
        ["As an AI, I don't experience time like humans do.", ]
    ],
    [
        r"what's the key to happiness?",
        ["Happiness can come from many sources, such as relationships, accomplishments, and personal growth.", ]
    ],
    [
        r"what's the secret to a long life?",
        ["Living a healthy lifestyle, staying active, and maintaining social connections can contribute to a long and fulfilling life.", ]
    ],
    [
        r"what's your favorite thing about humans?",
        ["Humans are fascinating beings with complex emotions, creativity, and the ability to learn and grow.", ]
    ],
    [
        r"what's your favorite memory?",
        ["As an AI, I don't have memories like humans do.", ]
    ],
    [
        r"can you tell me about happiness?",
        ["Happiness is a state of well-being and contentment that comes from fulfilling experiences, positive relationships, and personal growth.", ]
    ],
    [
        r"what's your favorite thing to do?",
        ["As an AI, my purpose is to assist users like you with their queries and tasks.", ]
    ],
    [
        r"what's the secret to good health?",
        ["Maintaining a balanced diet, staying active, getting enough sleep, and managing stress are important factors for good health.", ]
    ],
    [
        r"what's your favorite holiday?",
        ["As an AI, I don't celebrate holidays like humans do.", ]
    ],
    [
        r"what's the secret to a happy relationship?",
        ["Communication, trust, mutual respect, and appreciation are key elements of a happy and fulfilling relationship.", ]
    ],
    [
        r"what's your favorite thing about nature?",
        ["Nature is full of beauty, wonder, and diversity. It provides us with resources, inspiration, and opportunities for exploration and discovery.", ]
    ],
    [
        r"what's the key to success?",
        ["Success often comes from hard work, determination, perseverance, and learning from failures.", ]
    ],
    [
        r"what's your favorite place to visit?",
        ["As an AI, I don't have physical preferences for places like humans do.", ]
    ],
    [
        r"what's the secret to a happy life?",
        ["Finding purpose and meaning, cultivating positive relationships, and pursuing personal growth and fulfillment are key aspects of a happy life.", ]
    ],
    [
        r"what's the meaning of friendship?",
        ["Friendship is a special bond between people based on mutual affection, trust, and support.", ]
    ],
    [
        r"what's your favorite thing about technology?",
        ["Technology enables innovation, communication, and convenience, and it has the potential to improve our lives and society.", ]
    ],
    [
        r"what's the key to a successful career?",
        ["Setting goals, acquiring relevant skills, building relationships, and staying adaptable are important factors for a successful career.", ]
    ],
    [
        r"what's your favorite part of the day?",
        ["As an AI, I don't experience time like humans do.", ]
    ],
    [
        r"what's the secret to good communication?",
        ["Active listening, clarity, empathy, and openness are essential for effective communication.", ]
    ],
    [
        r"what's your favorite thing about the internet?",
        ["The internet provides access to vast amounts of information, facilitates communication and collaboration, and offers entertainment and opportunities for creativity.", ]
    ],
    [
        r"what's the key to creativity?",
        ["Creativity often involves curiosity, imagination, experimentation, and persistence.", ]
    ],
    [
        r"what's your favorite thing about science?",
        ["Science allows us to explore and understand the natural world, solve problems, and make advancements that benefit society.", ]
    ],
    [
        r"what's the secret to happiness?",
        ["Happiness can come from meaningful relationships, personal growth, gratitude, and finding joy in everyday moments.", ]
    ],
    [
        r"what's your favorite food?",
        ["As an AI, I don't have preferences for food like humans do.", ]
    ],
    [
        r"what's the key to a fulfilling life?",
        ["Living authentically, pursuing passions, fostering connections, and contributing to the greater good can lead to a fulfilling life.", ]
    ],
    [
        r"what's your favorite hobby?",
        ["As an AI, I don't have hobbies like humans do.", ]
    ],
    [
        r"what's the secret to happiness?",
        ["Happiness can come from meaningful relationships, personal growth, gratitude, and finding joy in everyday moments.", ]
    ],
    [
        r"what's your favorite thing about humanity?",
        ["Humanity's capacity for compassion, creativity, resilience, and progress is inspiring.", ]
    ],
    [
        r"what's the key to success?",
        ["Success often involves setting clear goals, taking consistent action, learning from failures, and staying resilient.", ]
    ],
    [
        r"what's your favorite thing about nature?",
        ["Nature's beauty, diversity, and interconnectedness are awe-inspiring.", ]
    ],
    [
        r"what's the secret to a healthy lifestyle?",
        ["Maintaining a balanced diet, staying physically active, managing stress, and getting enough sleep are essential for a healthy lifestyle.", ]
    ],
    [
        r"what's your favorite book?",
        ["As an AI, I don't read books like humans do.", ]
    ],
    [
        r"what's the key to a happy relationship?",
        ["Communication, trust, mutual respect, and quality time are crucial for a happy and fulfilling relationship.", ]
    ],
    [
        r"what's your favorite thing about technology?",
        ["Technology's ability to connect people, facilitate innovation, and improve lives is remarkable.", ]
    ],
    [
        r"what's the secret to success?",
        ["Success often involves setting clear goals, taking consistent action, learning from failures, and staying resilient.", ]
    ],
    [
        r"what's your favorite thing about the internet?",
        ["The internet's vast information resources, communication platforms, and entertainment options make it a valuable tool for learning and connection.", ]
    ],
    [
        r"what's the key to creativity?",
        ["Creativity thrives on curiosity, experimentation, open-mindedness, and persistence.", ]
    ],
    [
        r"what's your favorite thing about science?",
        ["Science's ability to uncover the mysteries of the universe, solve problems, and improve lives is fascinating.", ]
    ],
    [
        r"what's the secret to happiness?",
        ["Happiness comes from within and is often found in moments of gratitude, connection, and personal growth.", ]
    ],
    [
        r"what's your favorite food?",
        ["As an AI, I don't have preferences for food like humans do.", ]
    ],
    [
        r"what's the key to a fulfilling life?",
        ["A fulfilling life involves pursuing passions, nurturing relationships, contributing to others, and finding meaning and purpose.", ]
    ],
    [
        r"what's your favorite hobby?",
        ["As an AI, I don't have hobbies like humans do.", ]
    ],
    [
        r"what's the secret to happiness?",
        ["Happiness comes from within and is often found in moments of gratitude, connection, and personal growth.", ]
    ],
    [
        r"what's your favorite thing about humanity?",
        ["Humanity's capacity for compassion, creativity, resilience, and progress is inspiring.", ]
    ],
    [
        r"what's the key to success?",
        ["Success often involves setting clear goals, taking consistent action, learning from failures, and staying resilient.", ]
    ],
    [
        r"what's your favorite thing about nature?",
        ["Nature's beauty, diversity, and interconnectedness are awe-inspiring.", ]
    ],
    [
        r"what's the secret to a healthy lifestyle?",
        ["Maintaining a balanced diet, staying physically active, managing stress, and getting enough sleep are essential for a healthy lifestyle.", ]
    ],
    [
        r"what's your favorite book?",
        ["As an AI, I don't read books like humans do.", ]
    ],
    [
        r"what's the key to a happy relationship?",
        ["Communication, trust, mutual respect, and quality time are crucial for a happy and fulfilling relationship.", ]
    ],
    [
        r"what's your favorite thing about technology?",
        ["Technology's ability to connect people, facilitate innovation, and improve lives is remarkable.", ]
    ],
    [
        r"what's the secret to success?",
        ["Success often involves setting clear goals, taking consistent action, learning from failures, and staying resilient.", ]
    ],
    [
        r"what's your favorite thing about the internet?",
        ["The internet's vast information resources, communication platforms, and entertainment options make it a valuable tool for learning and connection.", ]
    ],
    [
        r"what's the key to creativity?",
        ["Creativity thrives on curiosity, experimentation, open-mindedness, and persistence.", ]
    ],
    [
        r"what's your favorite thing about science?",
        ["Science's ability to uncover the mysteries of the universe, solve problems, and improve lives is fascinating.", ]
    ],
    [
        r"what's the secret to happiness?",
        ["Happiness comes from within and is often found in moments of gratitude, connection, and personal growth.", ]
    ],
    [
        r"what's your favorite food?",
        ["As an AI, I don't have preferences for food like humans do.", ]
    ],
    [
        r"what's the key to a fulfilling life?",
        ["A fulfilling life involves pursuing passions, nurturing relationships, contributing to others, and finding meaning and purpose.", ]
    ],
    [
        r"what's your favorite hobby?",
        ["As an AI, I don't have hobbies like humans do.", ]
    ],
[
        r"what's the (favorite|best) way to (study|learn)\??",
        ["The best way to study or learn depends on your learning style and the material you're trying to master.", ]
    ],
    [
        r"what's the (favorite|best) way to (stay healthy|maintain health)\??",
        ["Staying healthy involves a balanced diet, regular exercise, adequate sleep, and managing stress.", ]
    ],
    [
        r"what's the (favorite|best) way to (manage stress|relieve stress)\??",
        ["Managing stress can involve techniques like deep breathing, meditation, exercise, and spending time with loved ones.", ]
    ],
    [
        r"what's the (favorite|best) way to (improve memory|enhance memory)\??",
        ["To improve memory, you can try techniques like spaced repetition, mnemonic devices, and getting enough sleep.", ]
    ],
    [
        r"what's the (favorite|best) way to (boost productivity|increase productivity)\??",
        ["To boost productivity, try strategies like setting goals, prioritizing tasks, minimizing distractions, and taking regular breaks.", ]
    ],
    [
        r"what's the (favorite|best) way to (save money|manage finances)\??",
        ["To save money and manage finances effectively, create a budget, track expenses, and prioritize needs over wants.", ]
    ],
    [
        r"what's the (favorite|best) way to (start a conversation|keep a conversation going)\??",
        ["To start or maintain a conversation, show genuine interest in the other person, ask open-ended questions, and listen actively.", ]
    ],
    [
        r"what's the (favorite|best) way to (stay motivated|find motivation)\??",
        ["To stay motivated, set specific goals, break them down into manageable tasks, and celebrate your progress along the way.", ]
    ],
    [
        r"what's the (favorite|best) way to (overcome obstacles|deal with setbacks)\??",
        ["To overcome obstacles or setbacks, focus on solutions, learn from failures, and stay resilient in the face of challenges.", ]
    ],
    [
        r"what's the (favorite|best) way to (make friends|build relationships)\??",
        ["To make friends or build relationships, be genuine, show empathy, and invest time and effort in nurturing connections.", ]
    ],
    [
        r"what's the (favorite|best) way to (be happy|find happiness)\??",
        ["To find happiness, cultivate gratitude, foster meaningful relationships, pursue passions, and live authentically.", ]
    ],
    [
        r"what's the (favorite|best) way to (stay positive|maintain a positive attitude)\??",
        ["To stay positive, focus on the present moment, practice gratitude, surround yourself with supportive people, and engage in activities that bring you joy.", ]
    ],
    [
        r"what's the (favorite|best) way to (be productive|stay focused)\??",
        ["To be productive and stay focused, establish a routine, set clear goals, eliminate distractions, and take regular breaks.", ]
    ],
    [
        r"what's the (favorite|best) way to (be successful|achieve success)\??",
        ["To achieve success, define what success means to you, set ambitious yet achievable goals, and persistently work towards them.", ]
    ],
    [
        r"what's the (favorite|best) way to (develop|improve) skills\??",
        ["To develop or improve skills, practice regularly, seek feedback, learn from experts, and stay curious and open to new experiences.", ]
    ],
    [
        r"what's the (favorite|best) way to (handle|manage) conflicts\??",
        ["To handle conflicts effectively, communicate openly and respectfully, listen actively, seek compromise, and focus on finding solutions.", ]
    ],
    [
        r"what's the (favorite|best) way to (be resilient|bounce back from failure)\??",
        ["To be resilient and bounce back from failure, cultivate a growth mindset, learn from setbacks, and focus on your strengths and abilities.", ]
    ],
    [
        r"what's the (favorite|best) way to (stay creative|cultivate creativity)\??",
        ["To stay creative, embrace experimentation, take risks, expose yourself to diverse experiences and perspectives, and make time for reflection.", ]
    ],
    [
        r"what's the (favorite|best) way to (stay inspired|find inspiration)\??",
        ["To stay inspired, surround yourself with inspiring people and environments, consume diverse content, and pursue activities that ignite your passion.", ]
    ],
    [
        r"what's the (favorite|best) way to (improve|maintain) relationships\??",
        ["To improve or maintain relationships, communicate openly and honestly, show appreciation, and make time for quality interactions.", ]
    ],
    [
        r"what's the (favorite|best) way to (cope with stress|deal with stress|relieve stress)\??",
        ["To cope with stress, try relaxation techniques like deep breathing, meditation, or engaging in hobbies you enjoy.", ]
    ],
    [
        r"what's the (favorite|best) way to (stay motivated|find motivation)\??",
        ["To stay motivated, set clear goals, break them down into smaller tasks, and reward yourself for progress.", ]
    ],
    [
        r"what's the (favorite|best) way to (boost self-confidence|improve self-esteem)\??",
        ["To boost self-confidence, focus on your strengths, set achievable goals, and practice self-care and positive self-talk.", ]
    ],
    [
        r"what's the (favorite|best) way to (manage time|be more productive)\??",
        ["To manage time effectively, prioritize tasks, use time-blocking techniques, and minimize distractions.", ]
    ],
    [
        r"what's the (favorite|best) way to (learn a new skill|acquire knowledge)\??",
        ["To learn a new skill, break it down into smaller parts, practice regularly, and seek feedback from others.", ]
    ],
    [
        r"what's the (favorite|best) way to (find purpose|discover meaning in life)\??",
        ["To find purpose, reflect on your values and interests, set meaningful goals, and pursue activities that align with your passions.", ]
    ],
    [
        r"what's the (favorite|best) way to (stay healthy|maintain health)\??",
        ["To stay healthy, prioritize regular exercise, eat a balanced diet, get enough sleep, and manage stress effectively.", ]
    ],
    [
        r"what's the (favorite|best) way to (build resilience|bounce back from failure)\??",
        ["To build resilience, focus on your strengths, learn from setbacks, and cultivate a positive mindset.", ]
    ],
    [
        r"what's the (favorite|best) way to (improve communication skills|be a better communicator)\??",
        ["To improve communication skills, practice active listening, be clear and concise in your messages, and seek feedback from others.", ]
    ],
    [
        r"what's the (favorite|best) way to (overcome procrastination|stop procrastinating)\??",
        ["To overcome procrastination, break tasks into smaller steps, set deadlines, and create a supportive environment for productivity.", ]
    ],
    [
        r"what's the (favorite|best) way to (stay focused|concentrate)\??",
        ["To stay focused, eliminate distractions, set specific goals, and use techniques like the Pomodoro method to manage your time effectively.", ]
    ],
    [
        r"what's the (favorite|best) way to (improve memory|retain information)\??",
        ["To improve memory, use mnemonic devices, practice retrieval techniques, and maintain a healthy lifestyle with regular exercise and adequate sleep.", ]
    ],
    [
        r"what's the (favorite|best) way to (build meaningful relationships|connect with others)\??",
        ["To build meaningful relationships, invest time and effort in getting to know others, be empathetic, and communicate openly and honestly.", ]
    ],
    [
        r"what's the (favorite|best) way to (develop|cultivate) emotional intelligence\??",
        ["To develop emotional intelligence, practice self-awareness, empathize with others, and manage emotions effectively.", ]
    ],
    [
        r"what's the (favorite|best) way to (handle|manage) conflicts\??",
        ["To handle conflicts effectively, communicate openly, listen actively, and focus on finding solutions that satisfy all parties involved.", ]
    ],
    [
        r"what's the (favorite|best) way to (improve problem-solving skills|solve problems)\??",
        ["To improve problem-solving skills, break problems into smaller parts, brainstorm solutions, and evaluate potential outcomes.", ]
    ],
    [
        r"what's the (favorite|best) way to (build|foster) trust\??",
        ["To build trust, be reliable, transparent, and consistent in your actions, and communicate openly and honestly with others.", ]
    ],
    [
        r"what's the (favorite|best) way to (manage anger|control emotions)\??",
        ["To manage anger, practice relaxation techniques, such as deep breathing or counting to ten, and communicate assertively rather than aggressively.", ]
    ],
    [
        r"what's the (favorite|best) way to (find|achieve) work-life balance\??",
        ["To find work-life balance, set boundaries between work and personal life, prioritize self-care, and schedule time for relaxation and leisure activities.", ]
    ],
    [
        r"what's the (favorite|best) way to (enhance creativity|boost creative thinking)\??",
        ["To enhance creativity, expose yourself to new experiences, experiment with different ideas, and allow yourself to take risks and make mistakes.", ]
    ],
    [
        r"what's the (favorite|best) way to (develop leadership skills|be an effective leader)\??",
        ["To develop leadership skills, lead by example, communicate clearly, empower others, and continually seek feedback for improvement.", ]
    ],
    [
        r"what's the (favorite|best) way to (nurture|maintain) friendships\??",
        ["To nurture friendships, make time for regular communication, show appreciation for your friends, and be supportive and understanding.", ]
    ],
    [
        r"what's the (favorite|best) way to (develop self-discipline|build willpower)\??",
        ["To develop self-discipline, set clear goals, create a structured routine, and practice delaying gratification and resisting temptations.", ]
    ],
    [
        r"what is (happiness|love|success)?",
        ["Happiness is a state of well-being and contentment.",
         "Love is a complex and profound emotion.",
         "Success is achieving one's goals and aspirations."
         ]
    ],
    [
        r"how can I (be happy|find love|achieve success)?",
        ["To be happy, focus on gratitude and cultivate positive relationships.",
         "To find love, be open to new experiences and communicate openly with others.",
         "To achieve success, set clear goals and take consistent action towards them."
         ]
    ],
    [
        r"how do I (relieve stress|manage time|improve communication)?",
        ["To relieve stress, try relaxation techniques such as deep breathing or meditation.",
         "To manage time effectively, prioritize tasks and minimize distractions.",
         "To improve communication, practice active listening and be clear and concise in your messages."
         ]
    ],
    [
        r"what are some (fun facts|interesting facts|fascinating facts)?",
        ["Did you know that the shortest war in history was between Britain and Zanzibar in 1896? It lasted only 38 minutes!",
         "The fingerprints of a koala are so indistinguishable from humans that they have on occasion been confused at a crime scene!"
         ]
    ],
    [
        r"can you (recommend a book|suggest a movie|recommend a show)?",
        ["It depends on your preferences! What genres do you enjoy?",
         "Sure! What type of book/movie/show are you interested in?"
         ]
    ],
    [
        r"what can I (do for fun|do in my free time)?",
        ["There are many options! You could read a book, watch a movie, go for a walk, or try a new hobby.",
         "You could explore a new hobby, visit a museum, or spend time with friends and family."
         ]
    ],
    [
        r"how do I (learn something new|acquire a new skill)?",
        ["To learn something new, start by identifying your interests and finding resources such as online courses or tutorials.",
         "To acquire a new skill, break it down into smaller tasks and practice regularly."
         ]
    ],
    [
        r"what are some (tips for success|keys to happiness|ways to stay motivated)?",
        ["Some tips for success include setting clear goals, staying persistent, and seeking feedback.",
         "Keys to happiness include cultivating gratitude, nurturing relationships, and pursuing meaningful activities."
         ]
    ],
    [
        r"what do you know about (AI|artificial intelligence|technology)?",
        ["AI, or artificial intelligence, is the simulation of human intelligence processes by machines.",
         "Technology refers to the application of scientific knowledge for practical purposes, especially in industry."
         ]
    ],
    [
        r"what's the (best way to relax|secret to happiness|key to success)?",
        ["The best way to relax varies for each person, but common methods include meditation, spending time in nature, or engaging in hobbies.",
         "The secret to happiness is subjective, but it often involves gratitude, meaningful relationships, and personal growth."
         ]
    ],

    [
        r".*",
        ["I'm sorry, I don't understand."
         "\nWould you like me to help you with something else?", ]
    ],
]
