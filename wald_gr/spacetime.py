import matplotlib.pyplot as plt
import math

N = 10
t = [i for i in range(int(-N/2),int(N/2)+1)]
c = 1

def gamma(v):
    return math.sqrt(1 - v**2 / c**2)

def LorentzX(x, v):
    x_prime = (x - v * t) / gamma(v)
    return x_prime

def LorentzT(x, v):
    t_prime = (t - (v * x / c**2)) / gamma(v)
    return t_prime

def PlotLightSignal(axs, x_0, t_0, sign="pos"):
    if sign == "neg":
        light_cone_x = [-i+x_0 if i >= 0 else None for i in t]
    else:
        light_cone_x = [i+x_0 if i >= 0 else None for i in t]
    light_cone_t = [i+t_0 if i >= 0  else None for i in t]
    axs.plot(light_cone_x, light_cone_t, 'y', alpha=0.4)

def PlotSpaceTimeDiagram(axs, garage, car):
    axs.plot(garage[0], t, 'r', label='Garage front')
    axs.plot(garage[1], t, 'g', label='Garage back')
    axs.plot(car[0], t, 'b', label='Car back')
    axs.plot(car[1], t, 'k', label='Car front')

    axs.legend()

def main():
    garage_length = 2

    garage_front = [0] * int(N+1)
    garage_back = [garage_length] * int(N+1)

    v_car = 0.5
    car_length = gamma(v_car) * garage_length
    car_back = [v_car * i for i in t]
    car_front = [i + car_length for i in car_back]

    fig, axs = plt.subplots(1, 2, sharex=True, sharey=True)
    axs[0].title.set_text("Garage Frame")

    axs[0].annotate('  A_0', (0,0))
    axs[0].annotate('  A_1', (0,garage_length))
    axs[0].annotate('  B', (garage_length,0))
    PlotLightSignal(axs[0], 0, 0, "pos")
    PlotLightSignal(axs[0], 0, 0, "neg")
    PlotLightSignal(axs[0], garage_length, 0, "neg")
    PlotLightSignal(axs[0], 2, (2-car_length)/v_car, "neg")
    axs[0].annotate('  C', (2, (2-car_length)/v_car))
    #axs[0].plot(2, (2-car_length)/v_car, 'ro')
    PlotSpaceTimeDiagram(axs[0], [garage_front, garage_back],\
                                  [car_front, car_back])

    x_prime = [LorentzX(i, v_car) for i in garage_front]
    y_prime = [LorentzT(i, v_car) for i in t]

    car_length = 2
    car_back = [0] * int(N+1)
    car_front = [car_length] * int(N+1)

    v_garage = -0.5

    garage_length = gamma(v_car) * car_length
    garage_front = [v_garage * i for i in t]
    garage_back = [i + garage_length for i in garage_front]
    axs[1].title.set_text("Car Frame")
    axs[1].annotate('  A_0', (0,0))
    axs[1].annotate('  A_1', (0,car_length))
    axs[1].annotate('  B', (car_length,0))
    PlotLightSignal(axs[1], car_length, 0, "neg")
    axs[1].annotate('  C', (2, (2-garage_length)/v_garage))
    #axs[0].plot(2, (2-car_length)/v_car, 'ro')
    PlotSpaceTimeDiagram(axs[1], [garage_front, garage_back],\
                                  [car_front, car_back])
    plt.show()
    '''
    plt.title('Garage reference frame')
    plt.plot(garage_front, t, 'r', label='Garage front')
    plt.plot(garage_back, t, 'g', label='Garage back')
    plt.plot(car_back, t, 'b', label='Car back')
    plt.plot(car_front, t, 'k', label='Car front')

    plt.plot(light_cone, t, 'y')
    plt.plot([-1*i for i in light_cone], t, 'y', label='Light cone')

    plt.legend()
    plt.xlim(-N/2, N/2)
    plt.ylim(-N/2, N/2)
    plt.gca().set_aspect('equal')
    plt.show()
    '''

if __name__ == "__main__":
    main()
