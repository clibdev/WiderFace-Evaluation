# Fork of [wondervictor/WiderFace-Evaluation](https://github.com/wondervictor/WiderFace-Evaluation)

Differences between original repository and fork:

* Original WIDERFace dataset annotations from GitHub [releases page](https://github.com/clibdev/WiderFace-Evaluation/releases). (🔥)
* Installation with [requirements.txt](requirements.txt) file.
* The following deprecations and warnings has been fixed:
  * DeprecationWarning: 'np.float' is a deprecated alias for builtin 'float'.
  * FutureWarning: Cython directive 'language_level' not set.
  * Cython Warning: Using deprecated NumPy API.

# Annotations

* Download links:

| Name                         | Link                                                                                                            | SHA-256                                                          |
|------------------------------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| wider_easy_val.mat           | [GitHub](https://github.com/clibdev/WiderFace-Evaluation/releases/latest/download/wider_easy_val.mat)           | c2fb672d16f75653eb89fb8bc437a7d060896a71cd7a65c1a5a3e4479024099c |
| wider_medium_val.mat         | [GitHub](https://github.com/clibdev/WiderFace-Evaluation/releases/latest/download/wider_medium_val.mat)         | 4a031970bc132cef5cfacd05068aabcf4fe15d4a31a1e9f4f00eb134fdf449c1 |
| wider_hard_val.mat           | [GitHub](https://github.com/clibdev/WiderFace-Evaluation/releases/latest/download/wider_hard_val.mat)           | bb1af19dc5bc4dd9517dd8ae8096326c68175f2c3411763bdd4f23fa98638b78 |
| wider_face_val.mat           | [GitHub](https://github.com/clibdev/WiderFace-Evaluation/releases/latest/download/wider_face_val.mat)           | 1dfe6a9853950f9dde256b5e8bb75d8f272e6bc02a15ae1968f5a9b883f458cb |
| wider_face_val_bbx_gt.txt    | [GitHub](https://github.com/clibdev/WiderFace-Evaluation/releases/latest/download/wider_face_val_bbx_gt.txt)    | 5ca83488f72758ca4826c35212610a8abf04a7af7b17eb407d6284007baba3b6 |
| wider_face_val_gt.txt        | [GitHub](https://github.com/clibdev/WiderFace-Evaluation/releases/latest/download/wider_face_val_gt.txt)        | bb19c548fbe81c9b459b53f6d5ed8286f5fd6e97a9c7c0edbd5ad64a6900f26c |
| wider_face_test.mat          | [GitHub](https://github.com/clibdev/WiderFace-Evaluation/releases/latest/download/wider_face_test.mat)          | 5efe15956d675ebc738bd4e9e249ca18d4a41866b5c40aa87c48225656636895 |
| wider_face_test_filelist.txt | [GitHub](https://github.com/clibdev/WiderFace-Evaluation/releases/latest/download/wider_face_test_filelist.txt) | 5ce69938c5149eff5ab814d737f9095c129fe42a86e672c94024f86fc879ae6d |
| wider_face_train.mat         | [GitHub](https://github.com/clibdev/WiderFace-Evaluation/releases/latest/download/wider_face_train.mat)         | 49fe14265426fbd5e4a8355f91717150fa26986029545fc7af20ea642f71d6fa |
| wider_face_train_bbx_gt.txt  | [GitHub](https://github.com/clibdev/WiderFace-Evaluation/releases/latest/download/wider_face_train_bbx_gt.txt)  | 753a8c0591cc570a793bb7fd2de4db6e5357bb1abbe863d8739d586369e32d9d |

# Installation

```shell
pip install -r requirements.txt
```

# WIDERFace Evaluation

* Run prediction on validation set and save results in the `results` directory.
* From releases page download `wider_easy_val.mat`, `wider_medium_val.mat`, `wider_hard_val.mat`,
  and `wider_face_val.mat` file to `ground_truth` directory.
* Build extension:

```shell
python setup.py build_ext --inplace
```

* Start evaluation:

```shell
python evaluation.py
```
