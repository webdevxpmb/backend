# PMB API Guide

## Sections

* [Installation](#installation)
* [Endpoints](#endpoints)
* [Models](#models)
* [Login Explanation](#login-explanation)

## Installation

[Back to sections](#sections)

This API use Python 2.7

Ini cara install di local
* Pull repository backend
* Cd ke folder backendnya
* Uncomment di backend/cas_views.py untuk pakai library yg python 2.7
  * So far sih ini aja, tp kalo nanti ada yang lain pasti ditandain '# For Python 2.7gii'
* Buat virtual environment baru yang versi Python-nya 2.7
  * DI TERMINAL : pip2 install virtualenv
  * DI TERMINAL : virtualenv < your virtual environment folder > --python=python2.7
    * Contoh : virtualenv venv --python=python2.7
* Activate virtual environment, caranya
  * DI TERMINAL : source < your virtual environment folder >/bin/activate
    * Contoh : source venv/bin/activate
  * Harusnya disamping nama username kalian ada tulisan (< your virtual environment folder name >)
    * Contoh : (venv) anthrocoon12@julius-graucus
* Semua command dibawah dalam kondisi virtualenv aktif
* DI TERMINAL : pip install -r requirements.txt
* DI TERMINAL : python manage.py makemigrations
* (Better safe than sorry) DI TERMINAL : python manage.py makemigrations account kenalan website
* DI TERMINAL : python manage.py migrate
* DI TERMINAL : python manage.py seed
* Buat jalanin server, DI TERMINAL : python manage.py runserver
  * Usually jalannya di localhost:8000, kalo somehow your port not available, tambahin aja portnya dibelakang
    * Contoh : python manage.py runserver < your port number here >

## Endpoints

[Back to sections](#sections)

For now, liat di Models dulu details spesifikasinya

### Endpoints List

============================================================

* [Authentication](#authentication)
* [User Related](#user-related)
* [Announcement and Post](#announcement-and-post)
* [Task and Submission](#task-and-submission)
* [Event](#event-endpoints)
* [Apa Kata Elemen](#apa-kata-elemen)
* [Kenalan, Token, and Friends](#kenalan,-token,-and-friends)
* [Statistics](#statistics)

============================================================

* ### Authentication
  [Back to endpoints list](#endpoints-list)
  * > GET **/pmb-api/login/**
  * > GET **/pmb-api/logout/**

* ### User Related

  [Back to endpoints list](#endpoints-list)
  
  ============================================================

  **Model used -> [User](#user)**

  * > GET POST **/pmb-api/user/**

    **Permission Classes:** IsPmbAdmin

    JSON lihat dibawah (Perbedaannya kalo disini jadi list aja)

  * > GET PUT PATCH DELETE **/pmb-api/user/{id-dari-usernya}/**

    **Permission Classes:** IsPmbAdmin

    Probably yang bakal dipakai cuma GET, karena edit profile di endpoint lain  
    **JSON**:
    ```json
    {
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
          "email": "pande.ketut71@ui.ac.id",
          "photo": "http://ristek.cs.ui.ac.id/pmb-api/media/ice_bear"
      }
    }
    ```

  ============================================================

  **Model used => [UserProfile](#userprofile)**

  * > GET POST **/pmb-api/user-profile/**

    **Permission Classes:** IsAuthenticated

    Kalo mau add user profile manual lewat sini  
    JSON lihat dibawah (Perbedaannya kalo disini jadi list trus role dan angkatan cuma idnya aja)

  * > GET PUT PATCH DELETE **/pmb-api/user-profile/{id-dari-userprofilenya}**

    **Permission Classes:** IsAuthenticated (GET), IsOwner (PUT, PATCH, DELETE)

    Probably POST ga dipakai, karena user profile auto-generate pas user login  
    * Role auto diassign jadi maba (for maba obviously) dan elemen (untuk sisanya)  
    * Role admin diassign manual
    * Default assignment :
      * photo, asal_sekolah, link_gdrive, line_id, phone_number, birth_place, birth_date diassign **null**
      * about diassign **empty string**
      * score diassign **0.0**

    **JSON**:
    ```json
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
      "asal_sekolah": null,
      "link_gdrive": null,
      "line_id": null,
      "phone_number": null,
      "birth_place": null,
      "birth_date": null,
      "score": 0.0,
      "created_at": "2018-07-02T23:54:20.976634",
      "updated_at": "2018-07-02T23:58:23.347770"
    }
    ```

  ============================================================

  **Model used => [Role](#role)**

  * > GET POST **/pmb-api/role/**

    **Permission Classes:** IsPmbAdmin

    Role udah di seed jadi probably ga bakal POST manual  
    JSON lihat dibawah (bedanya cuma disini jadi list)

  * > GET PUT PATCH DELETE **/pmb-api/role/{id-dari-rolenya}/**

    **Permission Classes:** IsPmbAdmin
  
    **JSON**:
    ```json
      {
        "id": 2,
        "role_name": "admin"
      }
    ```

  ============================================================

  **Model used => [Angkatan](#angkatan)**

  * > GET POST **/pmb-api/angkatan/**

    **Permission Classes:** IsPmbAdmin

    Angkatan udah di seed jadi probably ga bakal POST manual  
    JSON lihat dibawah (bedanya cuma disini jadi list)

  * > GET PUT PATCH DELETE **/pmb-api/angkatan/{id-dari-angkatannya}/**
  
    **JSON:**
    ```json
    {
      "id": 26,
      "year": "2018",
      "name": "2018"
    }
    ```

  ============================================================

* ### Announcement and Post

  [Back to endpoints list](#endpoints-list)

  ============================================================

  **Model used => [Post](#post)**

  **Ini satu set mirip semua, perbedaannya cuma kalo announcement dia querynya cuma ngembaliin yang PostType-nya Pengumuman aja dan kalo mau add post baru apapun jenisnya, selalu lewat /pmb-api/post/**
  
  **Query String buat GET:**

  * post_type -> filter by type
  * author__profile__angkatan -> filter by angkatan yang buat postnya

  Example:  
  > **/pmb-api/post/?=post_type=pengumuman&author__profile__angkatan=tarung**

  Ambil semua post bertipe pengumuman yang dibuat anak tarung

  * > GET **/pmb-api/announcement/**

    **Permission Classes:** IsAuthenticated
  
    *JSON lihat dibawah (virtually sama, cuma kalo ini query yg pengumuman aja lalu dan post tetep lewat bawah)

  * > GET POST **/pmb-api/post/**

    **Permission Classes:** IsAuthenticated (GET), IsPmbAdmin (POST)

    Tetap kalo POST cuma single object
    * Required : content dan post_type
    * post_type itu id dari post_typenya
    * title boleh null tapi ga boleh blank (empty string)
    * cover_image_link, summary, attachment_link boleh null dan blank (empty string)
    * author diambil dari request
    * created_at, updated_at auto generated

    JSON:  
    Ini hasil dari **http://127.0.0.1:8000/pmb-api/announcement/**,
    ```json
    [
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
                  "email": "pande.ketut71@ui.ac.id",
                  "photo": "http://ristek.cs.ui.ac.id/pmb-api/media/ice_bear"
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
      }
    ]
    ```

    POST Kalo ngepost cukup kayak gini
    ```json
    {
        "title": "PENGUMUMAN CAHYA",
        "cover_image_link": null,
        "summary": "cahya itu ganteng",
        "content": "cahya ganteng banget",
        "post_type": 1,
        "attachment_link": null
    }
    ```
  
  * > GET PUT PATCH DELETE **/pmb-api/post/{id-dari-postnya}/**

    **Permission Classes:** IsAuthenticated (GET), IsOwner (sisanya)

    JSON lihat diatas (cuma satu object aja, bukan list, spesifikasi json sama)

  ============================================================

  **Model used => [PostType](#posttype)**

  * > GET POST **/pmb-api/post-type/**

    **Permission Classes:** IsPmbAdmin

    JSON lihat bawah (as usual, bedanya cuma dia di list dan kalo add baru cuma satu object and lewat sini)

  * > GET PUT PATCH DELETE **/pmb-api/post-type/{id-dari-posttypenya}/**

    **Permission Classes:** IsPmbAdmin

    JSON:  
    ```json
    {
      "id": 1,
      "post_type": "pengumuman"
    }
    ```

  ============================================================  

* ### Task and Submission

  [Back to endpoints list](#endpoints-list)

  ============================================================

  **Model used => [Task](#task)**

  * > GET POST **/pmb-api/task/**

    **Permission Classes:** IsAuthenticated (GET), IsPmbAdmin (POST)

    JSON lihat bawah (as usual, bedanya cuma dia di list dan kalo add baru cuma satu object and lewat sini)

  * > GET PUT PATCH DELETE **/pmb-api/task/{id-dari-tasknya}/**

    **Permission Classes:** IsAuthenticated (GET), IsOwner (sisanya)

    * Required: start_time and end_time
    * name boleh null, tapi ga boleh blank (empty_string)
    * sisanya boleh null, boleh blank, default null
    * isKenalan auto false kalo ga diisi
    * as usual, created_at and updated_at autogenerated

    **JSON:**
    ```json
    {
        "id": 1,
        "name": "Task Cahyo",
        "description": "Kumpulkan sebanyak mungkin merchandise Ice Bear",
        "start_time": "2018-06-15T00:00:00",
        "attachment_link": null,
        "end_time": "2018-08-03T16:37:39",
        "is_kenalan": false,
        "expected_amount_tarung": null,
        "expected_amount_omega": null,
        "expected_amount_capung": null,
        "expected_amount_alumni": null,
        "created_at": "2018-08-03T16:37:49.872308",
        "updated_at": "2018-08-03T16:37:49.872326"
    }
    ```

    Kalo POST bisa kayak gini (add other fields as needed, such as isKenalan kalo ini task Kenalan and so on) :
    ```json
    {
        "name": "Task Cahyo",
        "description": "Kumpulkan sebanyak mungkin merchandise Ice Bear",
        "start_time": "2018-06-15T00:00:00",
        "end_time": "2018-08-03T16:37:39"
    }
    ```

  ============================================================

  **Model used => [Task QnA](#task-qna)**

  * > GET POST **/pmb-api/qna/**

    **Permission Classes:** IsAuthenticated (GET, POST)

    **Query String**
    > /?task=1

    Contoh : GET /pmb-api/qna/?task=1 : Akan mengembalikan list of QnA untuk task yang idnya 1

    JSON lihat bawah (as usual, bedanya cuma dia di list dan kalo add baru cuma satu object and lewat sini)

  * > GET PUT PATCH DELETE **/pmb-api/qna/{id-dari-qnanya}/**

    **Permission Classes:** IsOwner (All)

    * Required: task, comment
    * as usual, created_at and updated_at autogenerated

    **JSON:**
    ```json
    {
      "id": 1,
      "task": {
          "id": 1,
          "name": "Task Cahyo",
          "description": "Kumpulkan sebanyak mungkin merchandise Ice Bear",
          "start_time": "2018-06-15T00:00:00",
          "attachment_link": null,
          "end_time": "2018-08-12T16:37:39",
          "is_kenalan": true,
          "expected_amount_tarung": null,
          "expected_amount_omega": null,
          "expected_amount_capung": null,
          "expected_amount_alumni": null,
          "created_at": "2018-08-03T16:37:49.872308",
          "updated_at": "2018-08-03T16:47:59.146163"
      },
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
              "email": "pande.ketut71@ui.ac.id",
              "photo": "http://ristek.cs.ui.ac.id/pmb-api/media/ice_bear"
          }
      },
      "comment": "Waduh kok unreasonable tasknya kak?",
      "created_at": "2018-08-09T15:49:12.624429",
      "updated_at": "2018-08-09T15:49:12.624452"
    }
    ```

    Kalo POST kayak gini :
    ```json
    {
      "task": 1,
      "comment": "Waduh kok unreasonable tasknya kak?"
    }
    ```
    
  ============================================================

  **Model used => [Submission](#submission)**

  **Semua submission beserta semua fieldnya hanya ditampilkan  di django-admin**  
  Kalo lewat API, yang bisa di GET cuma submission punya sendiri (walaupun kamu superuser, staff, pmbadmin, tetap cuma submission sendiri yang bisa di GET)  
  Ada 2 additional field yang ga ditampilin kalau lewat API, yaitu is_checked and is_approved

  * > GET POST **/pmb-api/submission/**

    **Permission Classes:** IsMabaOrAdmin

    JSON lihat bawah (as usual, bedanya cuma dia di list dan kalo add baru cuma satu object and lewat sini)

  * > GET PUT PATCH DELETE **/pmb-api/submission/{id-dari-submissionnya}/**

    **Permission Classes:** IsOwner

    * user langsung diambil dari request
    * user dan task bukan cuma id doang
    * file_link boleh null (seriously boleh)

    **JSON:**
    ```json
    {
        "id": 2,
        "user": {
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
                "email": "pande.ketut71@ui.ac.id",
                "photo": "http://ristek.cs.ui.ac.id/pmb-api/media/ice_bear"
            }
        },
        "task": {
            "id": 1,
            "name": "Task Cahyo",
            "description": "Kumpulkan sebanyak mungkin merchandise Ice Bear",
            "start_time": "2018-06-15T00:00:00",
            "attachment_link": null,
            "end_time": "2018-08-03T16:37:39",
            "is_kenalan": true,
            "expected_amount_tarung": null,
            "expected_amount_omega": null,
            "expected_amount_capung": null,
            "expected_amount_alumni": null,
            "created_at": "2018-08-03T16:37:49.872308",
            "updated_at": "2018-08-03T16:47:59.146163"
        },
        "file_link": "www.miniso.com"
    }
    ```

    Kalo POST kayak gini:
    ```json
    {
      "task": 1,
      "file_link": "www.miniso.com"
    }
    ```

  ============================================================

* ### Event Endpoints

  [Back to endpoints list](#endpoints-list)

  ============================================================

  **Model used => [Event](#event)**

  * > GET POST **/pmb-api/event/**

    **Permission Classes:** IsAuthenticated (GET), IsPmbAdmin (POST)

    JSON lihat bawah (as usual, bedanya cuma dia di list dan kalo add baru cuma satu object and lewat sini)

  * > GET PUT PATCH DELETE **/pmb-api/event/{id-dari-eventnya}/**

    **Permission Classes:** IsAuthenticated (GET), IsPmbAdmin (sisanya)

    * Required: location (yep location doang)
    * description, start_time, end_time, attachment_link boleh null boleh blank
    * name dan expected_attendee boleh null tapi ga boleh blank
    * as usual, created_at and updated_at autogenerated

    **JSON:**
    ```json
    {
        "id": 2,
        "name": "Gabut di kantor Part 1",
        "description": "Gunakan lah waktu gabut anda di kantor dengan baik, contohnya dengan mengerjakan tugas",
        "location": "Kantor masing-masing",
        "start_time": "2018-08-09T16:03:39",
        "end_time": "2018-08-24T18:00:00",
        "expected_attendee": 11,
        "attachment_link": "www.gabut.com",
        "created_at": "2018-08-09T16:05:42.712187",
        "updated_at": "2018-08-09T16:05:42.712205"
    }
    ```

    Kalo POST bisa kayak gini (add other fields as needed) :
    ```json
    {
        "name": "Gabut di kantor Part 1",
        "description": "Gunakan lah waktu gabut anda di kantor dengan baik, contohnya dengan mengerjakan tugas",
        "location": "Kantor masing-masing",
        "start_time": "2018-08-09T16:03:39",
        "end_time": "2018-08-24T18:00:00",
        "expected_attendee": 11,
        "attachment_link": "www.gabut.com"
    }
    ```

* ### Apa Kata Elemen

  [Back to endpoints list](#endpoints-list)

  ============================================================

  **Model used => [Element Word](#element-word)**

  * > GET POST **/pmb-api/element-word/**

    **Permission Classes:** IsAuthenticated (GET), IsElemenOrAdmin (POST)

    JSON lihat bawah (as usual, bedanya cuma dia di list dan kalo add baru cuma satu object and lewat sini)

  * > GET PUT PATCH DELETE **/pmb-api/element-word/{id-dari-element-wordnya}/**

    **Permission Classes:** IsOwner (All)

    * Required: testimony
    * approved defaultnya false (sepertinya intended buat di approve lewat django admin)
    * author as usual dari request, dan kalo get di expand
    * as usual, created_at and updated_at autogenerated

    **JSON:**
    ```json
    {
        "id": 1,
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
                "email": "pande.ketut71@ui.ac.id",
                "photo": "http://ristek.cs.ui.ac.id/pmb-api/media/ice_bear"
            }
        },
        "testimony": "PMB mantap",
        "approved": false,
        "created_at": "2018-08-09T17:10:22.466032",
        "updated_at": "2018-08-09T17:10:22.466063"
    }
    ```

    Kalo POST bisa kayak gini (add other fields as needed) :
    ```json
    {
        "testimony": "PMB mantap"
    }
    ```

* ### Kenalan, Token, and Friends

  [Back to endpoints list](#endpoints-list)

  ============================================================

  Buat yang mau test di local, inget **python manage.py seed_kenalan_status**

  Alur Kenalan:
  * Si Elemen GET **/pmb-api/generate-token/** (Gw lihatnya kalo tahun lalu dia di homepage langsung nembak ini)
  * Si Maba POST **/pmb-api/create-kenalan/** dengan data {"token": "token-elemennya"}
  * API bakal balikin objek ~~detail~~ kenalannya (RALAT), yang isinya like this (DEFAULT STATUSNYA ITU 4: SAVED) 
    ```json
    {
      "detail_kenalan": {
        "id": 5,
        "name": "Pande Ketut Cahya Nugraha",
        "phone_number": null,
        "birth_place": null,
        "birth_date": null,
        "asal_sma": null,
        "story": null,
        "created_at": "2018-08-28T15:30:40.205635",
        "angkatan": null,
        "link_photo": null,
        "updated_at": "2018-08-28T15:30:40.205696"
      },
      "id": 5,
      "user_elemen": {
        "id": 2,
        "username": "pande.ketut71",
        "profile": {
          "id": 2,
          "user": 2,
          "name": "Pande Ketut Cahya Nugraha",
          "role": {
              "id": 2,
              "role_name": "elemen"
          },
          "npm": "1706028663",
          "angkatan": {
              "id": 6,
              "year": "2018",
              "name": "2018"
          },
          "email": "pande.ketut71@ui.ac.id",
          "photo": null,
          "about": "",
          "asal_sekolah": "SMAN 3 Denpasar",
          "link_gdrive": null,
          "line_id": "SSS",
          "phone_number": "81999749715",
          "birth_place": null,
          "birth_date": null,
          "score": 0,
          "created_at": "2018-08-27T14:51:16.184388",
          "updated_at": "2018-08-27T14:51:16.184453",
          "photo_url": null
        }
      },
      "user_maba": {
        "id": 2,
        "username": "pande.ketut71",
        "profile": {
          "id": 2,
          "user": 2,
          "name": "Pande Ketut Cahya Nugraha",
          "role": {
              "id": 2,
              "role_name": "elemen"
          },
          "npm": "1706028663",
          "angkatan": {
              "id": 6,
              "year": "2018",
              "name": "2018"
          },
          "email": "pande.ketut71@ui.ac.id",
          "photo": null,
          "about": "",
          "asal_sekolah": "SMAN 3 Denpasar",
          "link_gdrive": null,
          "line_id": "SSS",
          "phone_number": "81999749715",
          "birth_place": null,
          "birth_date": null,
          "score": 0,
          "created_at": "2018-08-27T14:51:16.184388",
          "updated_at": "2018-08-27T14:51:16.184453",
          "photo_url": null
        }
      },
      "status": {
        "id": 4,
        "status": "saved"
      },
      "notes": null,
      "created_at": "2018-08-28T15:30:39.758627",
      "updated_at": "2018-08-28T15:30:39.758653"
    }
    ```
  * Yang diedit bagian detail_kenalan pakai PATCH ke **/pmb-api/detail-kenalan/{id-detail-kenalannya}/**
  
  Endpoints

  * > GET **/pmb-api/generate-token/**

    **Permission Classes:** IsElemen

    Ngebalikin JSON ini
    **JSON**
    ```json
    {
      "token": "016377",
      "user": {
          "id": 2,
          "username": "pande.ketut71",
          "profile": {
              "id": 1,
              "name": "Pande Ketut Cahya Nugraha",
              "npm": "1706028663",
              "angkatan": {
                  "id": 4,
                  "year": "2017",
                  "name": "tarung"
              },
              "email": "pande.ketut71@ui.ac.id",
              "photo": null,
              "photo_url": null
          }
      },
      "start_time": "2018-08-20T22:19:55.661427",
      "end_time": "2018-08-20T22:24:55.661427",
      "created_at": "2018-08-20T22:19:55.661427",
      "updated_at": "2018-08-20T22:19:55.661427"
    }
    ```
  
  * > POST **/pmb-api/create-kenalan/**

    **Permission Classes:** IsMaba

    Request Bodynya ini:
    ```json
    {
      "token": "016377"
    }
    ```

    Ngebalikin ini:
    * Note that user_elemen sama user_maba itu seharusnya pasangan unik
    * Status -> 1: Accepted, 2: Pending, 3: Rejected, 4: Saved
    * Nanti abis edit detail_kenalan tembaknya ke **/pmb-api/detail-kenalan/{id-detail-kenalannya}/**
    * NOTE : Ini object kenalan yang dibalikinnya, kalo detail kenalan itu cuma yang di field
    "detail_kenalan"
    * NOTE : Ga bisa langsung edit di **/pmb-api/kenalan/{id-kenalan}** karena detail_kenalan kalo POST cuma nerima id doang
    ```json
    {
      "detail_kenalan": {
          "id": 4,
          "name": "Pande Ketut Cahya Nugraha",
          "phone_number": null,
          "birth_place": null,
          "birth_date": null,
          "asal_sma": null,
          "story": null,
          "created_at": "2018-08-20T22:20:19.656012",
          "angkatan": null,
          "link_photo": null,
          "updated_at": "2018-08-20T22:20:19.656012"
      },
      "id": 4,
      "user_elemen": {
          "id": 2,
          "username": "pande.ketut71",
          "profile": {
              "id": 1,
              "user": 2,
              "name": "Pande Ketut Cahya Nugraha",
              "role": {
                  "id": 2,
                  "role_name": "elemen"
              },
              "npm": "1706028663",
              "angkatan": {
                  "id": 4,
                  "year": "2017",
                  "name": "tarung"
              },
              "email": "pande.ketut71@ui.ac.id",
              "photo": null,
              "about": null,
              "asal_sekolah": null,
              "link_gdrive": null,
              "line_id": null,
              "phone_number": null,
              "birth_place": null,
              "birth_date": null,
              "score": 0,
              "created_at": "2018-07-22T20:52:13.990834",
              "updated_at": "2018-07-22T20:52:13.990859",
              "photo_url": null
          }
      },
      "user_maba": {
          "id": 2,
          "username": "pande.ketut71",
          "profile": {
              "id": 1,
              "user": 2,
              "name": "Pande Ketut Cahya Nugraha",
              "role": {
                  "id": 2,
                  "role_name": "elemen"
              },
              "npm": "1706028663",
              "angkatan": {
                  "id": 4,
                  "year": "2017",
                  "name": "tarung"
              },
              "email": "pande.ketut71@ui.ac.id",
              "photo": null,
              "about": null,
              "asal_sekolah": null,
              "link_gdrive": null,
              "line_id": null,
              "phone_number": null,
              "birth_place": null,
              "birth_date": null,
              "score": 0,
              "created_at": "2018-07-22T20:52:13.990834",
              "updated_at": "2018-07-22T20:52:13.990859",
              "photo_url": null
          }
      },
      "status": {
          "id": 2,
          "status": "pending"
      },
      "notes": null,
      "created_at": "2018-08-20T22:20:19.536696",
      "updated_at": "2018-08-20T22:20:19.536696"
    }
    ```

    * > GET POST **/pmb-api/detail-kenalan/**

    **Permission Classes:** IsAuthenticated

    JSON lihat dibawah (as usual, bedanya cuma dia di list dan kalo add baru cuma satu object and lewat sini)  
    Oh, and setiap user cuma bisa ngelist detail kenalan punyanya dia sendiri  
    List Detail kenalan sepertinya tidak intended buat di GET samsek

    * > GET PUT PATCH DELETE **/pmb-api/detail-kenalan/{id-detail-kenalannya}/**

    **Permission Classes:** IsDetailKenalanOwner

    **json**
    ```json
    {
        "id": 5,
        "kenalan": {
            "id": 5,
            "user_elemen": 2,
            "user_maba": 2,
            "status": 2,
            "notes": null
        },
        "name": "Pande Ketut Cahya Nugraha",
        "phone_number": null,
        "birth_place": null,
        "angkatan": null,
        "link_photo": null,
        "birth_date": null,
        "asal_sma": null,
        "story": null,
        "created_at": "2018-08-28T15:30:40.205635",
        "updated_at": "2018-08-28T15:30:40.205696"
    }
    ```

    * > GET POST **/pmb-api/kenalan/**

    **Permission Classes:** IsAuthenticated

    JSONnya sama kayak yang dibalikin sama **/pmb-api/create-kenalan/**, cuma kalo disini list  
    Kalo Maba yang nge GET, ngebalikin semua kenalan, tapi kalo Elemen yang nge GET, ngebalikin kenalan yang statusnya bukan 4 (Saved) alias non-draft  
    
    * > GET PATCH PUT DELETE **/pmb-api/kenalan/{id-kenalan}**

    **Permission Classes:** IsKenalanOwner

    Kalo mau ubah status, tembak ke sini, kalo ubah detail kenalan (kayak nama, nomer hp, story, etc.) itu tembak ke **/pmb-api/detail-kenalan/{idnya}**
    
    ============================================================

* ### Statistics

  [Back to endpoints list](#endpoints-list)

  ============================================================

  * > GET **/pmb-api/task-statistic/**

    **Permission Classes:** IsAuthenticated (GET)

    Sepertinya amount itu intendednya buat di set sama PMB Admin buat nunjukin berapa orang 
    yang udah submit atau belom

    **json**
    ```json
    [
      {
        "id": 3,
        "task": {
          "id": 3,
          "name": "Kenalan",
          "description": "Perlukan saya teriak 666 setiap jam 12 malem supaya backendnya tidak bermasalah aneh?",
          "start_time": "2018-08-27T14:52:43",
          "attachment_link": null,
          "end_time": "2018-08-31T14:52:45",
          "is_kenalan": true,
          "expected_amount_tarung": 15,
          "expected_amount_omega": 15,
          "expected_amount_capung": 15,
          "expected_amount_alumni": 15,
          "created_at": "2018-08-27T14:52:50.794702",
          "updated_at": "2018-08-27T14:52:50.794745"
        },
        "amount": 0,
        "created_at": "2018-08-27T14:52:50.831091",
        "updated_at": "2018-08-27T14:52:50.831159"
      }
    ]
    ```

    * > GET **/pmb-api/user-statistic/**

    **Permission Classes:** IsAuthenticated (GET)

    So, kalo ada bikin task kenalan, ntar tiap maba dibuatin object user statistic
    yang ngetrack jumlah kenalan dia.

    **json**
    ```json
    [
      {
        "id": 1,
        "user": 2,
        "name": "Kenalan statistic",
        "task": {
            "id": 3,
            "name": "Kenalan",
            "description": "Perlukan saya teriak 666 setiap jam 12 malem supaya backendnya tidak bermasalah aneh?",
            "start_time": "2018-08-27T14:52:43",
            "attachment_link": null,
            "end_time": "2018-08-31T14:52:45",
            "is_kenalan": true,
            "expected_amount_tarung": 15,
            "expected_amount_omega": 15,
            "expected_amount_capung": 15,
            "expected_amount_alumni": 15,
            "created_at": "2018-08-27T14:52:50.794702",
            "updated_at": "2018-08-27T14:52:50.794745"
        },
        "amount_omega": 0,
        "amount_capung": 0,
        "amount_orion": 0,
        "amount_alumni": 0,
        "amount_approved_omega": 0,
        "amount_approved_capung": 0,
        "amount_approved_orion": 0,
        "amount_approved_alumni": 0
      }
    ]
    ```

    * > GET **/pmb-api/event-statistic/**
    
    **Permission Classes:** IsAuthenticated (GET)

    Dibuat manual sama PMB Admin

    **json**
    ```json
    [
      {
        "id": 1,
        "event": {
            "id": 1,
            "name": "Berdoa agar website baik-baik saja",
            "description": "Seminggu pengen main game nih",
            "location": "Rumah Masing-Masing",
            "start_time": "2018-08-27T00:00:00",
            "end_time": "2018-12-31T00:00:00",
            "expected_attendee": 11,
            "attachment_link": null,
            "created_at": "2018-08-27T15:07:17.218986",
            "updated_at": "2018-08-27T15:07:17.219048"
        },
        "attendee": 11,
        "on_time": 11,
        "late": 0,
        "permission": 0,
        "absent": 0,
        "created_at": "2018-08-27T15:07:26.435946",
        "updated_at": "2018-08-27T15:07:26.436005"
      }
    ]
    ```

    * > GET **/pmb-api/task-score/**

    **Permission Classes:** IsAuthenticated (GET)

    Untuk setiap task yang di-set ke is_scored, dibuatin taskScore

    **json**
    ```json
    [
      {
        "id": 1,
        "user": 2,
        "name": "Kenalan score",
        "task": {
          "id": 3,
          "name": "Kenalan",
          "description": "Perlukan saya teriak 666 setiap jam 12 malem supaya backendnya tidak bermasalah aneh?",
          "start_time": "2018-09-12T07:05:59",
          "attachment_link": null,
          "end_time": "2018-11-30T23:55:00",
          "is_kenalan": true,
          "expected_amount_tarung": 0,
          "expected_amount_omega": 15,
          "expected_amount_capung": 15,
          "expected_amount_alumni": 15,
          "expected_amount_bebas": null,
          "created_at": "2018-08-27T14:52:50.794702",
          "updated_at": "2018-09-27T19:47:09.819184"
        },
        "score": 0,
        "comment": "Bagus sekali"
      }
    ]
    ```

  ============================================================

## Models

[Back to sections](#sections)

### Daftar Models

============================================================

* [User](#user)
* [UserProfile](#userprofile)
* [ShrinkedUserProfile](#shrinkeduserprofile)
* [Post](#post)
* [PostType](#posttype)
* [Task](#task)
* [Task QnA](#task-qna)
* [Submission](#submission)
* [Event](#event)
* [Element Word](#element-word)

============================================================

* ### User

  [Back to Daftar Models](#daftar-models)

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

  [Back to Daftar Models](#daftar-models)

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
  * asal_sekolah:
    * type: string
    * maxLength: 100
  * link_gdrive:
    * type: string
    * maxLength: 100
  * line_id:
    * type: string
    * maxLength: 100
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

  [Back to Daftar Models](#daftar-models)

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
  * photo
    * type: string

* ### Post  

  [Back to Daftar Models](#daftar-models)

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

  [Back to Daftar Models](#daftar-models)
  
  Fields:
  * id  
    * type : integer  
    * Tidak dibutuhkan saat POST, auto-generated  
  * **post_type**  
    * type : string  

* ### Task

  [Back to Daftar Models](#daftar-models)

  Fields:
  * id
    * type : integer
    * auto-generated
  * name
    * type : string
    * maxLength: 255
    * minLength: 1
  * description
    * type : string
  * **start_time**
    * type : string date-time
  * attachment_link
    * type : string
    * maxLength: 255
  * **end_time**
    * type : string date-time
  * is_kenalan
    * type : boolean
  * expected_amount_tarung
    * type : integer
  * expected_amount_omega
    * type : integer
  * expected_amount_capung
    * type : integer
  * expected_amount_alumni
    * type : integer
  * created_at
    * type : string date-time
  * updated_at
    * type : string date-time

* ### Task QnA

  Fields:
  * id
  * **task**
    * type: integer
    * ID dari model Task
    * Wajib ada di JSONnya
    * Expanded pas get
  * author
    * type: integer
    * ID dari model User
    * Auto generated
    * Expanded pas get
  * **comment**
    * type : string
  * created_at
    * type : string date-time
  * updated_at
    * type : string date-time

* ### Submission

  [Back to Daftar Models](#daftar-models)

  Fields:
  * id
    * type: integer
  * user
    * type: integer
    * expanded pas di GET
  * **task**
    * type: integer
    * expanded pas di GET
  * file_link
    * type: string
    * maxLength: 255
    * minLength: 1

* ### Event

  Fields:
  * id
    * type: integer
  * name
    * type: string
    * maxLength: 255
    * minLength: 1
  * description
    * type: string
  * **location**
    * type: string
    * maxLength: 255
    * minLength: 1
    * WAJIB
  * start_time
    * type : string date-time
  * end_time
    * type : string date-time
  * attachment_link 
    * type: string
    * maxLength: 255
    * minLength: 1
  * expected_attendee
    * type: integer
  * created_at
    * type : string date-time
  * updated_at
    * type : string date-time

* ### Element Word

  Fields:

  Note:  
  Defaultnya ada dua PostType, yaitu Pengumuman dan Post Biasa  
  Untuk PostType Pengumuman, nama dari post_type nya adalah 'pengumuman'  
  Untuk PostBiasa, nama dari post_type nya adalah 'post biasa'

### Login Explaination

[Back to sections](#sections)

Karena kita login menggunakan SSO UI, loginnya agak ribet (?).  
Basically stepsnya kayak gini:  

* Frontend buka new window login yg urlnya ke endpoint login
* Frontend komunikasi dengan window login pake postMessage
* Setelah berhasil login sso, window login buat sebuah var yg isinya token sama data user,
  lalu window login send postMessage ke Frontend buat nandain proses login udh selesai
* Frontend manggil fungsi yang fetch var user dari window login, lalu close window login  

Details bisa dilihat di [sini](https://github.com/webdevxpmb/frontend/blob/master/app/containers/LoginPage/index.js)
