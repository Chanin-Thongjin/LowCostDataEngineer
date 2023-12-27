# LOW COST DATA PIPELINE
![Alt text](/image/pipeline.png)

## Step
1. Create Big Query
2. Create Cloud Function, 
   >2.1 set the type of trigger is Cloud Pub/Sub  set Topic (Can create new topic)
   <img src="./image/trigger.png" width="400">

   >2.2 set runtime environment variables
   <img src="./image/environment.png" width="400">

   >2.3 set Code

   <img src="./image/Code.png" width="400">

   > 2.4 set requirements
   <img src="./image/requirements.png" width="400">

3. Create Google Cloud Schedule and test crick Run
   
   <img src="./image/Schedule.png" width="400">
   <img src="./image/Schedule-1.png" width="400">
4. Check on Big Query
   
   <img src="./image/Check.png" width="400">
   
## About total the cost in the pipeline
- Bigquery : use 5 GB/month in this case we insert 1 row assume 1 KB that it free for 5 million rows
- Cloud Function : Use 2 million/month free
- Cloud Pub/Sup : Use 50 GB/month free in this case we sended just "1".
- Cloud Schedule : Can have 3 schedule.
- Streaming insert in Cloud to Big Query : 
  $0.01/200 MB

## Referent
- https://github.com/fonylew/simple-cloud-functions-to-bigquery
- https://www.coindesk.com/coindesk-api
- https://api.coindesk.com/v1/bpi/currentprice/THB.json
- https://cloud.google.com/pricing?hl=en
