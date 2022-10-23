# ChessAI-PyGame ♟️
It's chess whith AI &amp; structure. I'll describe each action , specially captivating knew how artifitial work
<p align="center">
  <img src="https://media.giphy.com/media/r2qg4IWMJhtAc/giphy.gif">
</p>
<h2> ♟️ Main target </h2>
<p> It's to make an AI which can think how to do, that win & achieve lose of the opponent. This project, I was inspared playing games & I thought how to make bots which can exactly bit player -> don't make a superfluous action </p>
<h2> 🛠️ Development </h2>
<p> First of all, I create a <code>config.py</code> it's file need to write down several const. Therefore, I create a <code>main.py</code> where'll accure & call all functions. Inside main.py -> <b> class Main: </b> you can find a consructor which just render a screen. Likewise, you can find here <b> function mainloop ( ) </b> -> it is render game. Then I create a <code>GameEndine.py</code> -> which will describe <b> class Game: </b> -> function field ( )'ll create colorful pieces on the field. Run file to receive a result</p>
<p align="center">
  <img src="https://sun9-86.userapi.com/impg/IUCiK5LIyFKrqmM27u-wRPvTONmi_vwBEzL_yg/DUZ-Pkmmq5Y.jpg?size=1280x818&quality=96&sign=b605a29f3e408e427351be2b9cf58aed&type=album">
</p>
<p> Return inside file <code>GameEndine.py</code> to create <b> class Board & Square </b>. This class responsible to create 0 value - if no figure in this field or 1 - if there it is! Therefore, afore _ -> it's private method, thats mean only inside here you can used it. After this, lets create our pieces ( Pawn, Rook & etc. ). </p>
<p> I create file <code>piece.py</code> -> here I ll determine all pieces behaviour. For instance, lets create a mother class Piece -> from there they will take figures for their characteristics & create Pawn class. Inside pawn class describe -> color = white; value = 1.0 <b> value will be useful for ai which will determine which kill better Bishop or Pawn. <b> Self.dir - direction </b>, where & how many cells will go piece. </p>
<p align="center">
  <img src="https://sun9-4.userapi.com/impg/ljN_spKhbj7iPH5a7xVFW4vkKELMhx_eygBPuA/OgcR0gcCgb4.jpg?size=1280x775&quality=96&sign=61e09533bf9d88ebce891da422a869bc&type=album">
</p>
<p> <b>function set_texture</b> - represents images inside folder assets (images of pieces). I find a folder where lie this files & divided them into parts. </p>
<p align="center">
  <img src="https://sun9-38.userapi.com/impg/-8VTvqM_WEgQJ4D-KZaz1vWiGjemgU2AbD_V3w/1dnt2Vm33kY.jpg?size=752x790&quality=96&sign=70d3f575a82c0781eb8e010ccf8ee9a8&type=album">
</p>
<p>  </p>
