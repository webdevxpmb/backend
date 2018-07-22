# PMB API Guide

## Sections

* [Installation](#installation)
* [Endpoints](#endpoints)
* [Models](#models)
* [Login Explanation](#login-explanation)

## Installation

This API use Python 2.7

* Pull repository
* Buat virtual environment baru yang versi Python-nya 2.7
* Activate virtual environment (usually source < your virtual environment folder>/bin/activate)
* Run python manage.py makemigrations
* (Better safe than sorry) Run python manage.py makemigrations account kenalan website
* Run python manage.py migrate
* Run python manage.py seed
* To run server, python manage.py runserver

## Endpoints

For now, liat di Models dulu details spesifikasinya

* ### Authentication
  * GET /pmb-api/login/
  * GET /pmb-api/logout/

* ### User Related
  ============================================================  
  **Model used -> [User](#user)**
  * GET POST /pmb-api/user/  
  See below (Perbedaannya kalo disini jadi list aja)
  * GET PUT PATCH DELETE /pmb-api/user/< id >/  
  Probably yang bakal dipakai cuma GET, karena edit profile di endpoint lain  
  **JSON**:
    <pre>{
      "id": 11,
      "username": "pande.ketut71",
      "profile": {
          "id": 4,
          "name": "Pande Ketut Cahya Nugraha",
          "npm": "1706028663",
          "angkatan": {
              "id": 1,
              "year": "2017",
              "name": "tarung"
          },
          "email": "pande.ketut71@ui.ac.id"
      }
    }
    </pre>
  ============================================================
  * GET POST /pmb-api/user-profile/  
  Kalo mau add user profile manual lewat sini  
  See below (Perbedaannya kalo disini jadi list trus role dan angkatan cuma idnya aja)  
  * GET PUT PATCH DELETE /pmb-api/user-profile/< id >  
  Probably POST ga dipakai, karena user profile auto-generate pas user login  
  **JSON**:
    <pre>
    {
      "id": 4,
      "user": 11,
      "name": "Pande Ketut Cahya Nugraha",
      "role": {
          "id": 2,
          "role_name": "admin"
      },
      "npm": "1706028663",
      "angkatan": {
          "id": 1,
          "year": "2017",
          "name": "tarung"
      },
      "email": "pande.ketut71@ui.ac.id",
      "photo": null,
      "about": "",
      "linkedin": null,
      "facebook": null,
      "phone_number": null,
      "birth_place": null,
      "birth_date": null,
      "score": 0.0,
      "created_at": "2018-07-02T23:54:20.976634",
      "updated_at": "2018-07-02T23:58:23.347770"
    }
    </pre>

  ============================================================

  * GET POST /pmb-api/role/  
  Role udah di seed jadi probably ga bakal POST manual  
  See below (bedanya cuma disini jadi list)
  * GET PUT PATCH DELETE /pmb-api/role/< id >/  
  JSON:
    <pre>
    {
      "id": 2,
      "role_name": "admin"
    }
    </pre>

  ============================================================

  * GET POST /pmb-api/angkatan/  
  Angkatan udah di seed jadi probably ga bakal POST manual  
  See below (bedanya cuma disini jadi list)
  * GET PUT PATCH DELETE /pmb-api/angkatan/< id >/  
  JSON:
    <pre>
    {
      "id": 26,
      "year": "2018",
      "name": "2018"
    }
    </pre>

  ============================================================

* ### Announcement and Post

  ============================================================  
  Ini satu set mirip semua, perbedaannya cuma kalo announcement dia querynya cuma ngembaliin yang PostType-nya Pengumuman aja dan kalo mau add post baru apapun jenisnya, selalu lewat /pmb-api/post/  
  
  Query String buat GET:  
  post_type -> filter by type  
  author__profile__angkatan -> filter by angkatan yang buat postnya  
  page -> pagination  
  page_size -> tiap page mau berapa post  
  Example:  
  /pmb-api/post/?=post_type=pengumuman&author__profile__angkatan=tarung&page=1&page_size=2  
  Ambil semua post bertipe pengumuman yang dibuat anak tarung, page pertama dmn tiap page 2 post aja yang diambil
  * GET /pmb-api/announcement/  
  See below (virtually sama, cuma kalo ini query yg pengumuman aja lalu dan post tetep lewat bawah)
  * GET POST /pmb-api/post/  
  JSON:  
  Ini hasil dari "http://127.0.0.1:8000/pmb-api/announcement/?page=1&page_size=2",
    <pre>
    {
      "count": 4,
      "next": "http://127.0.0.1:8000/pmb-api/announcement/?page=2&page_size=2",
      "previous": null,
      "results": [
          {
              "id": 1,
              "title": "PENGUMUMAN CAHYA",
              "author": {
                  "id": 11,
                  "username": "pande.ketut71",
                  "profile": {
                      "id": 4,
                      "name": "Pande Ketut Cahya Nugraha",
                      "npm": "1706028663",
                      "angkatan": {
                          "id": 1,
                          "year": "2017",
                          "name": "tarung"
                      },
                      "email": "pande.ketut71@ui.ac.id"
                  }
              },
              "cover_image_link": null,
              "summary": "cahya itu ganteng",
              "content": "cahya ganteng banget",
              "post_type": {
                  "id": 1,
                  "post_type": "pengumuman"
              },
              "attachment_link": null,
              "created_at": "2018-07-04T17:22:08.119185",
              "updated_at": "2018-07-04T17:22:08.119213"
          },
          {
              "id": 3,
              "title": "Hai",
              "author": {
                  "id": 11,
                  "username": "pande.ketut71",
                  "profile": {
                      "id": 4,
                      "name": "Pande Ketut Cahya Nugraha",
                      "npm": "1706028663",
                      "angkatan": {
                          "id": 1,
                          "year": "2017",
                          "name": "tarung"
                      },
                      "email": "pande.ketut71@ui.ac.id"
                  }
              },
              "cover_image_link": null,
              "summary": "Summary",
              "content": "img src=x onerror=alert(1)//",
              "post_type": {
                  "id": 1,
                  "post_type": "pengumuman"
              },
              "attachment_link": null,
              "created_at": "2018-07-08T11:37:33.591104",
              "updated_at": "2018-07-08T11:37:33.591162"
          }
      ]
    }
    </pre>
  
  * GET PUT PATCH DELETE /pmb-api/post/< id >/  
  See above, ambil satu object aja

  ============================================================

  * GET POST /pmb-api/post-type/  
  See below (as usual, bedanya cuma dia di list dan kalo add baru lewat sini)
  * GET PUT PATCH DELETE /pmb-api/post-type/{id}/  
  JSON:  
    <pre>
    {
      "id": 1,
      "post_type": "pengumuman"
    }
    </pre>

  ============================================================

## Models

### Daftar Models

...............................  
[User](#user)  
[UserProfile](#userprofile)  
[ShrinkedUserProfile](#shrinkeduserprofile)  
[Post](#post)  
[PostType](#posttype)  
...............................  

* ### User
  Fields:
  * id
    * type: integer
  * username:
    * type: string
    * maxLength: 150
    * minLength: 1
  * profile:  
    **Disini dia nested object, ga cuma id doang**  
    See [ShrinkedUserProfile](#shrinkeduserprofile)  

* ### UserProfile  
  Fields:
  * id:
    * type: integer
  * user:
    * type: integer
    * **Ini cuma id dari Usernya**
  * name:
    * type: string
    * maxLength: 128
    * minLength: 1
  * role:
    * type: integer
    * **Ini cuma id dari role**
  * npm:
    * type: string
    * minLength: 1
  * angkatan:
    * type: integer
    * **Ini cuma id dari angkatan**
  * email:
    * type: string
    * maxLength: 128
    * minLength: 1
  * photo:
    * type: string
    * format: uri
  * about:
    * type: string
  * linkedin:
    * type: string
    * maxLength: 128
  * facebook:
    * type: string
    * maxLength: 128
  * phone_number:
    * type: string
    * maxLength: 20
  * birth_place:
    * type: string
    * maxLength: 100
  * birth_date:
    * type: string date
  * score:
    * type: float
  * created_at:
    * type: string date-time
  * updated_at:
    * type: string date-time

* ### ShrinkedUserProfile  
  Fields:  
  * id:
    * type: integer
  * name:
    * type: string
    * maxLength: 128
    * minLength: 1
  * npm:
    * type: string
    * maxLength: 10
    * minLength: 1
  * angkatan:  
    **Disini dia ga cuma id aja, tapi nested object**
    * id:
      * type: integer
    * year:
      * type: string
      * maxLength: 50
      * minLength: 1
    * name:
      * type: string
      * maxLength: 50
      * minLength: 1
  * email:
    * type: string
    * maxLength: 128
    * minLength: 1

* ### Post  
  Fields:
  * id  
    * type : integer
    * Tidak dibutuhkan saat POST, auto-generated
  * **title**
    * type: string
    * maxLength: 255
    * minLength: 1
    * Wajib ada di JSONnya, tapi boleh null
  * author
    * type : integer
    * ID dari model User
    * Tidak dibutuhkan saat POST, diambil dari request.user
  * cover_image_link
    * type: string
    * maxLength: 255
  * summary  
    * type: string
    * maxLength: 255
  * **content**
    * type: string
    * minLength: 1
    * Wajib ada di JSONnya
  * **post_type**
    * type: integer
    * ID dari model PostType
    * Wajib ada di JSONnya
  * attachment_link
    * type: string
    * maxLength: 255
  * created_at
    * string date-time
    * Tidak dibutuhkan saat POST, auto-generated
  * updated_at
    * string date-time
    * Tidak dibutuhkan saat POST, auto-generated

* ### PostType  
  Fields:
  * id  
    * type : integer  
    * Tidak dibutuhkan saat POST, auto-generated  
  * **post_type**  
    * type : string  

  Note:  
  Defaultnya ada dua PostType, yaitu Pengumuman dan Post Biasa  
  Untuk PostType Pengumuman, nama dari post_type nya adalah 'pengumuman'  
  Untuk PostBiasa, nama dari post_type nya adalah 'post biasa'

### Login Explanation

Karena kita login menggunakan SSO UI, loginnya agak ribet (?).  
Basically stepsnya kayak gini:  

* Frontend buka new window login yg urlnya ke endpoint login
* Frontend komunikasi dengan window login pake postMessage
* Setelah berhasil login sso, window login buat sebuah var yg isinya token sama data user,
  lalu window login send postMessage ke Frontend buat nandain proses login udh selesai
* Frontend manggil fungsi yang fetch var user dari window login, lalu close window login  

Details bisa dilihat di [sini](https://github.com/webdevxpmb/frontend/blob/master/app/containers/LoginPage/index.js)