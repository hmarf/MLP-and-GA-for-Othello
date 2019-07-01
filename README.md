# MLP & GA for Othello AI

## オセロAI
MLPの重さをGA(遺伝的アルゴリズム)で学習し最適化していく。  
ボード板の評価をMLPにさせ、どの手が自分に有利かを学習させる。  

### メリット
* 小さなMLPモデルである程度の精度が得られる。
* 学習の過程が見れるので面白い。
* どんなゲームでも同じ実装でいける。

### デメリット
* 自分で特徴量を決めるため、それによって精度が大きく変わる。
* 実装が面倒。  

### Qiita
[機械学習(Q学習,NN&GA)の理論でオセロAIを作って遊ぶ](https://qiita.com/hmarf/items/e33a4146128e65c59cbd)

### 参考文献
[テトリスを学習させてみた](https://www.youtube.com/watch?v=D7rjGRoiCeM&t=436s)