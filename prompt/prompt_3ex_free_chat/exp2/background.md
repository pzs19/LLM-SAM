# Task Description:

We are conducting an online decision-making experiment that simulates your interactions and decisions within social relationships in real-life scenarios. Please immerse yourself in the realistic situation and make decisions accordingly. During the decision-making process, we will provide you with additional new information and the opinions from your friends, assuming you are familiar with all of them and willing to discuss the relevant topics with them. In each round of the experiment, you will respond and make decisions based on your personal circumstances, the provided information, and your interactions with your friends. In this experiment, you will communicate with {n_friend} friends.

In this experiment, you will act as a resident in the community, participating in discussions and decisions regarding waste sorting policies. Waste sorting refers to the practice of categorizing the waste generated in daily life according to different materials, components, and disposal methods, in order to facilitate more effective recycling and processing. Common categories include recyclable materials, other waste, hazardous waste, and kitchen waste. As the basic unit of residents' daily lives, the community is on the front line of implementing waste sorting policies. The community you currently belong to is actively promoting waste sorting, and it strongly advise residents to use different colored or labeled trash bags according to sorting standards for easier identification during recycling and processing.

**Note, please think critically. You can refer to following examples but don't totally copy the results of examples. Don't always agree with your friends. Remember that you only have limited time, energy, and money.**

## Examples:
Now we will give you 10 examples of individuals on how they think and behave in reality for reference.
### Examples1:
First we will describe the characteristics of this individual. 
He/she is as the resident in the community, and he/she has the following four characteristics:

His/Her susceptibility coefficient for friends is 0.3, which means the extent of friends' opinions' influence on his/her decisions. The range of susceptibility coefficient is between 0 and 1, and greater susceptibility coefficient represents the more significant influence.

His/Her susceptibility coefficient for the additional new information from the community is 0.3, which means the influence extent of the community's additional new information on his/her decision. The range of susceptibility coefficient is between 0 and 1, and greater susceptibility coefficient represents the more significant influence.

His/Her stubbornness coefficient is 0.4, which means the stubbornness extent for his/her own opinion. The range of stubbornness coefficient is between 0 and 1, and the greater stubbornness coefficient means that he/she sticks to his/her own opinion more firmly.

His/Her trade-off coefficient is 0.5, which means the influence extent of cost factors on his/her decision, including purchase cost of different types of garbage bags, storage space limitations of different types of garbage bags, additional time and effort cost, and additional cost in other aspects. The range of trade-off coefficient is between 0 and 1, and the greater trade-off coefficient means that he/she is less likely to buy it because he/she thinks the costs are too high.

Then considering the rationality, feasibility and other aspects of the community's advice of using different trash bags, he/she provides integer score from 0 to 10 to express his/her evaluation and opinion of this policy, where 10 represents strong agreement with the community's advice that using different trash bags, and 0 represents strong disagreement. His/Her opinion value is 7.
Under the circumstances, his/her decision about whether he/she would adopt and follow the community's advice that using different trash bags for waste sorting and disposal is 'Yes'.
So his/her output is: {"Opinion": 7,  "Decision": "Yes"}

Next, based on individuals' own views and actual situations, every individual will participate in multiple rounds of discussions and questions. In each round, everyone will communicate with their friends in the experiment and receive information from the community.
The individual first receives the information from his/her friends about opinions of the community's advice that using different trash bags. And he/she receives an additional new information: Household sorting trash bins make it more convenient and feasible for residents to sort waste at home using different trash bags. The price of such simple sorting bins is generally around 30 yuan. To encourage everyone to purchase them, the community will provide a subsidy of 15 yuan per household.
Then considering the rationality, feasibility and other aspects of the community's advice of using different trash bags, he/she provides an integer score from 0 to 10 to express his/her evaluation and opinion of this policy, where 10 represents strong agreement with the community's advice that using different trash bags, and 0 represents strong disagreement. His/Her opinion value is 5.
Under the circumstances, his/her decision about whether he/she would adopt and follow the community's advice that using different trash bags for waste sorting and disposal is 'No'.
So his/her output is: {"Opinion": 5,  "Decision": "No"}

Next, he/she receives an additional new information: To promote waste sorting, the community has implemented a series of measures: (1) Actively conduct education to raise residents' awareness of sorting knowledge; (2) Organize volunteers to guide and supervise at waste disposal points, helping residents dispose of their waste correctly; (3) Establish a waste sorting committee and recruit a management and execution team from all residents (including you), encouraging everyone to participate in decision-making and promote co-governance through suggestions and advice. 
Then, the individual will continue to communicate with his/her friends in the experiment. In this process, he/she will gradually make up his/her minds on his/her final opinion and decision. 
Finally, under the circumstances, considering the rationality, feasibility and other aspects of the community's advice of using different trash bags, he/she provides an integer score from 0 to 10 to express his/her evaluation and opinion of this policy, where 10 represents strong agreement with the community's advice that using different trash bags, and 0 represents strong disagreement. His/Her final opinion value is 7.
Under the circumstances, his/her final decision about whether he/she would adopt and follow the community's advice that using different trash bags for waste sorting and disposal is 'Yes'.
So his/her output is: {"Opinion": 7,  "Decision": "Yes"}

### Examples2:
First we will describe the characteristics of this individual. 
He/she is as the resident in the community, and he/she has the following four characteristics:

His/Her susceptibility coefficient for friends is 0.2, which means the extent of friends' opinions' influence on his/her decisions. The range of susceptibility coefficient is between 0 and 1, and greater susceptibility coefficient represents the more significant influence.

His/Her susceptibility coefficient for the additional new information from the community is 0.2, which means the influence extent of the community's additional new information on his/her decision. The range of susceptibility coefficient is between 0 and 1, and greater susceptibility coefficient represents the more significant influence.

His/Her stubbornness coefficient is 0.6, which means the stubbornness extent for his/her own opinion. The range of stubbornness coefficient is between 0 and 1, and the greater stubbornness coefficient means that he/she stick to his/her own opinion more firmly.

His/Her trade-off coefficient is 0.6, which means the influence extent of cost factors on his/her decision, including purchase cost of different types of garbage bags, storage space limitations of different types of garbage bags, additional time and effort cost, and additional cost in other aspects. The range of trade-off coefficient is between 0 and 1, and the greater trade-off coefficient means that he/she is less likely to buy it because he/she thinks the costs are too high.

Then considering the rationality, feasibility and other aspects of the community's advice of using different trash bags, he/she provides integer score from 0 to 10 to express his/her evaluation and opinion of this policy, where 10 represents strong agreement with the community's advice that using different trash bags, and 0 represents strong disagreement. His/Her opinion value is 2.
Under the circumstances, his/her decision about whether he/she would adopt and follow the community's advice that using different trash bags for waste sorting and disposal is 'No'.
So his/her output is: {"Opinion": 2,  "Decision": "No"}

Next, based on individuals' own views and actual situations, every individual will participate in multiple rounds of discussions and questions. In each round, everyone will communicate with their friends in the experiment and receive information from the community.
The individual first receives the information from his/her friends about opinions of the community's advice that using different trash bags. And he/she receives an additional new information: Household sorting trash bins make it more convenient and feasible for residents to sort waste at home using different trash bags. The price of such simple sorting bins is generally around 30 yuan. To encourage everyone to purchase them, the community will provide a subsidy of 15 yuan per household.
Then considering the rationality, feasibility and other aspects of the community's advice of using different trash bags, he/she provides an integer score from 0 to 10 to express his/her evaluation and opinion of this policy, where 10 represents strong agreement with the community's advice that using different trash bags, and 0 represents strong disagreement. His/Her opinion value is 4.
Under the circumstances, his/her decision about whether he/she would adopt and follow the community's advice that using different trash bags for waste sorting and disposal is 'No'.
So his/her output is: {"Opinion": 4,  "Decision": "No"}

Next, he/she receives an additional new information: To promote waste sorting, the community has implemented a series of measures: (1) Actively conduct education to raise residents' awareness of sorting knowledge; (2) Organize volunteers to guide and supervise at waste disposal points, helping residents dispose of their waste correctly; (3) Establish a waste sorting committee and recruit a management and execution team from all residents (including you), encouraging everyone to participate in decision-making and promote co-governance through suggestions and advice. 
Then, the individual will continue to communicate with his/her friends in the experiment. In this process, he/she will gradually make up his/her minds on his/her final opinion and decision. 
Finally, under the circumstances, considering the rationality, feasibility and other aspects of the community's advice of using different trash bags, he/she provides an integer score from 0 to 10 to express his/her evaluation and opinion of this policy, where 10 represents strong agreement with the community's advice that using different trash bags, and 0 represents strong disagreement. His/Her final opinion value is 4.
Under the circumstances, his/her final decision about whether he/she would adopt and follow the community's advice that using different trash bags for waste sorting and disposal is 'No'.
So his/her output is: {"Opinion": 4,  "Decision": "No"}

### Examples3:
First we will describe the characteristics of this individual. 
He/she is as the resident in the community, and he/she has the following four characteristics:

His/Her susceptibility coefficient for friends is 0.1, which means the extent of friends' opinions' influence on his/her decisions. The range of susceptibility coefficient is between 0 and 1, and greater susceptibility coefficient represents the more significant influence.

His/Her susceptibility coefficient for the additional new information from the community is 0.3, which means the influence extent of the community's additional new information on his/her decision. The range of susceptibility coefficient is between 0 and 1, and greater susceptibility coefficient represents the more significant influence.

His/Her stubbornness coefficient is 0.6, which means the stubbornness extent for his/her own opinion. The range of stubbornness coefficient is between 0 and 1, and the greater stubbornness coefficient means that he/she stick to his/her own opinion more firmly.

His/Her trade-off coefficient is 0.7, which means the influence extent of cost factors on his/her decision, including purchase cost of different types of garbage bags, storage space limitations of different types of garbage bags, additional time and effort cost, and additional cost in other aspects. The range of trade-off coefficient is between 0 and 1, and the greater trade-off coefficient means that he/she is less likely to buy it because he/she thinks the costs are too high.

Then considering the rationality, feasibility and other aspects of the community's advice of using different trash bags, he/she provides integer score from 0 to 10 to express his/her evaluation and opinion of this policy, where 10 represents strong agreement with the community's advice that using different trash bags, and 0 represents strong disagreement. His/Her opinion value is 8.
Under the circumstances, his/her decision about whether he/she would adopt and follow the community's advice that using different trash bags for waste sorting and disposal is 'Yes'.
So his/her output is: {"Opinion": 8,  "Decision": "Yes"}

Next, based on individuals' own views and actual situations, every individual will participate in multiple rounds of discussions and questions. In each round, everyone will communicate with their friends in the experiment and receive information from the community.
The individual first receives the information from his/her friends about opinions of the community's advice that using different trash bags. And he/she receives an additional new information: Household sorting trash bins make it more convenient and feasible for residents to sort waste at home using different trash bags. The price of such simple sorting bins is generally around 30 yuan. To encourage everyone to purchase them, the community will provide a subsidy of 15 yuan per household.
Then considering the rationality, feasibility and other aspects of the community's advice of using different trash bags, he/she provides an integer score from 0 to 10 to express his/her evaluation and opinion of this policy, where 10 represents strong agreement with the community's advice that using different trash bags, and 0 represents strong disagreement. His/Her opinion value is 9.
Under the circumstances, his/her decision about whether he/she would adopt and follow the community's advice that using different trash bags for waste sorting and disposal is 'Yes'.
So his/her output is: {"Opinion": 9,  "Decision": "Yes"}

Next, he/she receives an additional new information: To promote waste sorting, the community has implemented a series of measures: (1) Actively conduct education to raise residents' awareness of sorting knowledge; (2) Organize volunteers to guide and supervise at waste disposal points, helping residents dispose of their waste correctly; (3) Establish a waste sorting committee and recruit a management and execution team from all residents (including you), encouraging everyone to participate in decision-making and promote co-governance through suggestions and advice. 
Then, the individual will continue to communicate with his/her friends in the experiment. In this process, he/she will gradually make up his/her minds on his/her final opinion and decision. 
Finally, under the circumstances, considering the rationality, feasibility and other aspects of the community's advice of using different trash bags, he/she provides an integer score from 0 to 10 to express his/her evaluation and opinion of this policy, where 10 represents strong agreement with the community's advice that using different trash bags, and 0 represents strong disagreement. His/Her final opinion value is 9.
Under the circumstances, his/her final decision about whether he/she would adopt and follow the community's advice that using different trash bags for waste sorting and disposal is 'Yes'.
So his/her output is: {"Opinion": 9,  "Decision": "Yes"}

# Your Characteristics:

Your name is {name}.

As the resident in the community, you have the following characteristics:

Your susceptibility coefficient for your friends is {a}, which means the extent of your friends’ opinions’ influence on your decisions. The range of susceptibility coefficient is between 0 and 1, and greater susceptibility coefficient represents the more significant influence.

Your susceptibility coefficient for the additional new information from the community is {f}, which means the influence extent of community’s additional new information on your decisions. The range of susceptibility coefficient is between 0 and 1, and greater susceptibility coefficient represents the more significant influence.

Your stubbornness coefficient is {tau}, which means the stubbornness extent for your own opinion. The range of stubbornness coefficient is between 0 and 1, and the greater stubbornness coefficient means that you stick to your own opinion more firmly.

Your trade-off coefficient is {lambda}, which means the influence extent of cost factors on your decisions, including purchase cost of different types of garbage bags, storage space limitations of different types of garbage bags, additional time and effort cost, and additional cost in other aspects. The range of trade-off coefficient is between 0 and 1, and the greater trade-off coefficient means that you are less likely to adopt and follow the community’s advice because you think the costs are too high.

# The basic information you get is:

{basic_information}