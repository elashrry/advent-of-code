Let $t$ be the time you hold the button in milliseconds and $F$ the total
time of the race, then the distance your boat would move is

$$
\begin{split}
x &= t(F - t)\\
&= -t^2 + F t.
\end{split}
$$

Let $R$ be the best record, we are trying to find values of $t$ that satisfy the inequality

$$
\begin{aligned}
-t^2 + F t \gt R\\
-t^2 + F t - R \gt 0\\
t^2 - F t + R \lt 0.
\end{aligned}
$$

We notice the LHS is a parabola looking upward, then we are looking for integer values of $t$ lying strictly between the two real solutions of the quadratic equation $t^2 - F t + R$ while also being realistic, i.e., $0\lt t\lt F$.

This is under the assumption that the given input gives a quadratic equations with real solutions (unique or distinct), otherwise the problem doesn't make since.
