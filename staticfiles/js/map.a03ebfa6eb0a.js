function initMap() {
    // 检查google对象是否已经加载
    if (typeof google === 'object' && typeof google.maps === 'object') {
        // 从全局变量中获取经纬度
        const latitude = window.latitude || -34.397;
        const longitude = window.longitude || 150.644;
        const latLng = {lat: latitude, lng: longitude};
        const map = new google.maps.Map(document.getElementById('map'), {
            center: latLng,
            zoom: 6
        });

        const marker = new google.maps.Marker({
            position: latLng,
            map: map,
            draggable: true
        });

        document.getElementById('id_latitude').value = latitude.toFixed(15);
        document.getElementById('id_longitude').value = longitude.toFixed(15);

        marker.addListener('dragend', () => {
            const position = marker.getPosition();
            document.getElementById('id_latitude').value = position.lat().toFixed(15);
            document.getElementById('id_longitude').value = position.lng().toFixed(15);
        });

        map.addListener('click', (mapsMouseEvent) => {
            const clickedLatLng = mapsMouseEvent.latLng.toJSON();
            const formattedLat = clickedLatLng.lat.toFixed(15);
            const formattedLng = clickedLatLng.lng.toFixed(15);
            document.getElementById('id_latitude').value = formattedLat;
            document.getElementById('id_longitude').value = formattedLng;
            marker.setPosition(clickedLatLng);
        });
    } else {
        // 如果google对象不存在，输出错误到控制台
        console.error("Google Maps API is not loaded yet.");
    }
}