import numpy as np


class Params:
    def __init__(self, fx, fy, angle, dx, dy):
        self.fx = fx
        self.fy = fy
        self.angle = angle
        self.dx = dx
        self.dy = dy


def calPos(t, f, v):
    # f * t / 2 - 5 * f / 2 + 5 * v + (5 * f - 10 * v) * exp(-t / 5) / 2
    return f * t / 2 - 5 * f / 2 + 5 * v + (5 * f - 10 * v) * np.exp(-t / 5) / 2


def func(x, params):
    force = x[0]
    t = x[1]

    fx = params.fx
    fy = params.fy
    angle = params.angle
    dx = params.dx
    dy = params.dy

    vx = (force * np.cos(angle / 180 * np.pi) * 20)
    vy = (force * np.sin(angle / 180 * np.pi) * 20)

    f1 = calPos(t, fx, vx) - dx
    f2 = calPos(t, fy, vy) - dy

    return np.array([f1, f2])


def jacobian(x, params, h=1e-5):
    # Numerical approximation of the Jacobian matrix
    n = len(x)
    J = np.zeros((n, n))
    fx0 = func(x, params)

    for i in range(n):
        x1 = np.array(x, dtype=float)
        x1[i] += h
        fx1 = func(x1, params)
        J[:, i] = (fx1 - fx0) / h

    return J


def newton_method(x0, params, tol=1e-7, max_iter=1000):
    x = np.array(x0)
    for i in range(max_iter):
        f_val = func(x, params)
        if np.linalg.norm(f_val, ord=2) < tol:
            return x  # Solution found
        J = jacobian(x, params)
        try:
            delta = np.linalg.solve(J, -f_val)
        except np.linalg.LinAlgError:
            return None  # Jacobian is singular, no solution
        x = x + delta
    return None  # Did not converge


def calForce(angle: float, wind: float, dx: float, dy: float):
    params = Params(wind * 240, -7000, angle, dx * 100, dy * 100)

    # Initial guesses for force and time
    x_init = [50.0, 2.0]

    sol = newton_method(x_init, params)

    if sol is not None and 0 <= sol[0] <= 100:
        return sol[0]  # Return the force value
    else:
        return None


if __name__ == "__main__":
    for i in range(1, 21):
        force = calForce(0, 30, i, 0)
        if force is not None:
            print(f"dx: {i}\tforce: {force}")
        else:
            print(f"dx: {i}\tno solution")
