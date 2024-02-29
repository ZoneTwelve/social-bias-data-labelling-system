# social-bias-data-labelling-system

System Designs:
 - Label Data Structure:
    | Sentence ID | Biased Sentences | T-A Combination | Source | Identity | isBias | isMalice |
    | ----------- | ---------------- | --------------- | ------ | -------- | ------ | -------- |
    | 21398122    | 歐美的女人本來...  | 女人,老          | Ptt    | 女性      |[Boolean]|[Boolean]|
    | ...         | ...              | ...             | ...    | ...      |[Boolean]|[Boolean]|
-  System API
   - Users
     - Username
     - Password
     - Email
   - Questions
     - Sentence_id: [Auto Increase]:Integer
     - Biased Sentence: []:String
     - TAC: []:Array
     - Source: []:String
     - Identity: []:String
   - LabeledData
     - Label_id: [Auto Increase]:Integer
     - Sentence_id: []:Integer -> Questions.Sentence_id
     - isBias: []:Boolean
     - isMalice: []:Boolean
     - updateAt: []:Datetime
     - visitAt: []:Datetime
     - createAt: []:Datetime
