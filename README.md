# HighGunung-Engine
#### Informasi Teoritis, Teknis dan Praktis Lihat [wiki page](https://github.com/wimbuhAdi/HighGunung-Engine/wiki) untuk informasi lebih lengkap


## Lihat GuardianAngel dan WhatsappServer Beraksi
Video ini menampilkan module `GuardianAngel`, `WhatsappServer`, dan integrasi `TheThingsNetwork` via flow `Node-Red` bereaksi terhadap telemetri yang dikirimkan realtime oleh node-Lora. Sistem secara otomatis mengirimkan **pemberitahuan darurat** ke semua kontak penting di whatsapp.


[![Alt text](https://img.youtube.com/vi/sA308gRTwHI/0.jpg)](https://www.youtube.com/watch?v=sA308gRTwHI)



## Guardian Angel
me-return allert dengan memeriksa node's geo-location according to seted geolocation parameter berbentuk polygon. Terhubung dengan `WhatsappServer` via MQTT untuk membroadcast distress-message ke semua petugas
```
guardianAngel.py 
```


## Visualisasi Telemetry dan Dashboard
Menggunakan Node-red local server yang dapat diakses dalam satu network via browser. Terhubung langsung ke TTN sehingga data yang masuk dari node langsung di visualisasikan ke browser. 
### Node-red work-env
<p align="center">
  <img src="https://github.com/wimbuhAdi/HighGunung-Engine/blob/master/Node-red/Node-red_flow.jpg" alt="Size Limit CLI" width="750">
</p>

### Visualisasi realtime Node dan Node Telemetry
<p align="center">
  <img src="https://github.com/wimbuhAdi/HighGunung-Engine/blob/master/Node-red/visualisasi-node2.jpg" alt="Size Limit CLI" width="270">
  <img src="https://github.com/wimbuhAdi/HighGunung-Engine/blob/master/Node-red/nodeTelemetry-dashboard.jpg " alt="Size Limit CLI" width="350">
</p>


[Article reading](https://blog.mailtrap.io/send-emails-with-gmail-api/#How_to_make_your_app_send_emails_with_Gmail_API)    [google guide](https://developers.google.com/gmail/api/quickstart/python)
