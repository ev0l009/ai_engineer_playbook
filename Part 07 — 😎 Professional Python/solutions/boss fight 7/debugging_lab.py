#  |   | 

#  |  | 

#  |  | 

#  |  | 

#  |  | 

# |  | 

#  |  | 

#  |  | 

#  |  | return self

| Problem                                           | Why it's dangerous                                            | Professional fix                       |
|---------------------------------------------------|---------------------------------------------------------------|----------------------------------------|
| Missing type hints for arguments and return values.  | confusing as it's difficult to know what to expect and return | Add adequate type hints                |
| No player object validation in the add method.     | Partial initialization or storage of invalid data             | Validate player attributes during initialization.                |
| Duplicate players can be added.                    | Bloated database                                              | Add checks for duplicate registeration                |
| No argument validation in the find method.    | invalid arguments could be used which will crash the app      | check for invalid data type or empty string                |
| Potential runtime crash when find returns None.  | Invalid ratings could used                                    | Exception handling and is needed here to                |
| the update method does not check for valid rating | Using methods on a None return value triggers a crash.        | Add checks to validate rating                |
| No documentation.                                 | Methods become confusing, obscure, and difficult to maintain. | Use docstrings to provide concise useful information about the methods                |
| the top method doesn't handle an empty academy    | could crash if academy is empty                               | check the academy is not empty first before getting the top player                |
| minor design issue, some methods can retun self   | No exactly a bug in itself but reduce repitition              | return self                |