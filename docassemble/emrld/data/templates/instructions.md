[BOLDCENTER]Important Instructions


[STOP_INDENTATION]

Please keep a copy of these instructions and make sure you follow every step. 
If you fail to do any of these things your application may be refused!


Step 1:
Print out **${len(tenant)+len(landlord)+1}** copies of the application you have just made.


Step 2:
Print out **${len(tenant)+len(landlord)+1}** copies of all other evidence you said you will be submitting. 


Step 3:
It is important to label each piece of evidence.  Label them at the top of the page as Item A, Item B etc.  Here is the label you should put on each document:


% for x in evidence:
   Item ${x.name.text2}           ${x.name.text}

% endfor

Step 4:
Now we must make **${len(tenant)+len(landlord)+1}** packages.  The first document should be the application.  The second Item A, Item B, etc.  When you finish you should have **${len(tenant)+len(landlord)+1}** packages.


Step 5:
Bring all **${len(tenant)+len(landlord)+1}** packages with you to the RTDRS.  They will stamp all of them.  They will also take a copy for the office.  Then you will provide one to each tenant and each landlord.  One should go to each of the following people:

% for x in tenant:
${x.name.first} ${x.name.last}

% endfor
% for x in landlord:
${x.name.first} ${x.name.last}

% endfor


Step 6:
Deliver a copy of the package to each person mentioned in Step 5.