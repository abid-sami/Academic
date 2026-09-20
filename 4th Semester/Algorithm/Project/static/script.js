const car = document.getElementById("car");

function animateCar() {

    let points = [
        [100,250],
        [250,180],
        [450,180],
        [650,250]
    ];

    let i = 0;

    function move() {

        if(i >= points.length)
            return;

        car.setAttribute("cx", points[i][0]);
        car.setAttribute("cy", points[i][1]);

        i++;

        setTimeout(move, 800);
    }

    move();
}

function findRoute() {

    document.querySelectorAll("line").forEach(line=>{
        line.classList.remove("route");
    });

    document.getElementById("line1").classList.add("route");

    setTimeout(()=>{
        document.getElementById("line2").classList.add("route");
    },500);

    setTimeout(()=>{
        document.getElementById("line3").classList.add("route");
    },1000);

    animateCar();

    document.getElementById("result").innerHTML=
    "Shortest Route Found ✔️ <br> Distance: 7 KM";
}