<template>
  <v-container>
    <v-row class="mb-5">
      <v-col>
        <v-alert
          type="info"
          color="red"
          prominent
          variant="elevated"
        >
          <template #title>
            <div class="text-center w-100">
              Wir treffen uns neuerdings regelmäßig montags von 17:00 bis 18:30 Uhr <br>
              mit unserer Gruppe für Kinder von 7 bis 11 Jahren und suchen noch Verstärkung!<br>
              Komm du doch gerne mal vorbei!<br>
              Bei Fragen wende dich einfach an: <strong>nik @ hratuga.de</strong>
            </div>
          </template>
        </v-alert>
      </v-col>
    </v-row>
    <v-row
      v-for="({ title, text, img}, idx) in content"
      :key="title + idx"
      class="d-flex align-center justify-center mb-10 mb-lg-5"
    >
      <v-col
        cols="12"
        lg="6"
        order="1"
        :order-lg="2 - idx % 2"
      >
        <v-img
          :src="img"
          max-width="100%"
          class="rounded-lg elevation-6"
          cover
        />
      </v-col>
      <v-col
        cols="12"
        lg="6"
        order="2"
        :order-lg="1 + idx % 2"
      >
        <div class="text-h5 font-weight-black">
          {{ title }}
        </div>
        <p
          v-for="textContent in text"
          :key="textContent"
          class="mb-3"
        >
          {{ textContent }}
        </p>
        <v-btn
          v-if="idx === content.length - 1"
          variant="elevated"
          size="large"
          color="red"
          prepend-icon="mdi-hand-pointing-right"
          class="mt-3"
        >
          Hier geht's zu den Gruppen
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
const content = [
  {
    title: 'Pfadfindergruppe aus Ratingen-Homberg',
    text: ['Wir sind eine Pfadfindergruppe die seit 1982 in Ratingen Homberg Jugendarbeit betreibt. Wir haben ca. 60 Mitglieder und einige Gruppen mit Mitgliedern zwischen 7 und 20 Jahren. Die Details zu den Gruppen sind unter "Unsere Gruppen" zu finden.'],
    img: 'https://hratuga.de/static/img/2018-09-Horstlager-31.00b448e.jpg',
  },
  {
    title: 'Stamm Hratuga in Ratingen Homberg',
    text: [
      'Unser Pfadfinderstamm heißt Hratuga. Für viele ein merkwürdiger Name. Jedoch hat dieser einen völlig normalen Ursprung. Hratuga ist nämlich nicht anderes, als der mittelalterliche Name für die Stadt Ratingen, in welcher wir zu Hause sind. Genauer gesagt im Stadtteil Homberg.',
      'Bei uns treffen sich die Kinder- und Jugendlichen in wöchentlichen Gruppenstunden. Wir nennen diese Treffen: “Heimabend”. Dort wird zusammen gespielt, gekocht, die Natur entdeckt, die nächste Fahrt vorbereitet und natürlich auch Pfadfinderwissen erlernt. Schließlich muss man wissen, wie man ein Zelt aufbaut, sicher ein Lagerfeuer macht und sich in der Natur zurechtfindet. Dabei sind auch Themen vertreten, wie erste Hilfe oder auch kleine handwerkliche Arbeiten.',
    ],
    img: 'https://hratuga.de/static/img/image07.b38f687.jpg',
  },
  {
    title: 'Wer kann alles mitmachen?',
    text: [
      'Die Antwort ist sehr leicht. Jeder! Bei uns unterscheidet man Gruppen in drei Altersstufen:',
      'Die Wölflinge (ca. 7 bis 11 Jahre)',
      'Die Sippe (ca. 11 bis 16 Jahre)',
      'und die Rover (ca. 16+ Jahe)',
      'Diese Art von Gruppenbildungen ermöglichen gemeinsame Erlebnisse und Erfahrungen, um gemeinsam aufzublühen. Mit gleichaltrigen macht dies besonders viel Spaß!',
    ],
    img: 'https://hratuga.de/static/img/heim.2f9a2ca.jpg',
  },
  {
    title: 'Wölflinge?',
    text: [
      'Die meisten Kinder starten in der Wölflingsstufe. Dort bleiben sie so lange, bis sich einige gleichaltrige zu einer neuen Gruppe, der Sippe bilden. Hier, in der Meute, haben die Kinder die Chance sich auszutoben und trotzdem viel zu lernen und zu wachsen. Das Körperwachstum können wir leider nicht verhindern, wie wir oft mit Erschrecken feststellen müssen',
      'Diese Art von Gruppenbildungen ermöglichen gemeinsame Erlebnisse und Erfahrungen, um gemeinsam aufzublühen. Mit gleichaltrigen macht dies besonders viel Spaß!',
    ],
    img: 'https://hratuga.de/static/img/Robert%20(44%20von%20309).4788faf.jpg',
  },
  {
    title: 'Raus in die Natur',
    text: ['Natürlich sind wir Pfadfinder alles andere als Stubenhocker. „Raus in die Natur“ ist unser Motto. Darum sind wir viel draußen und es finden in regelmäßigen Abständen Fahrten statt. Im Winter gehts natürlich in ein Haus. Ziel ist neben dem Abenteuer auch, das gelernte Wissen anzuwenden und zu verbessern. Wie findet man einen guten Lagerplatz, wie baut man ein Zelt auf, oder wie kocht man über dem Feuer?'],
    img: 'https://hratuga.de/static/img/Robert%20(44%20von%20309).4788faf.jpg',
  },
  {
    title: 'Zeltlager und viele weitere Aktionen',
    text: ['Das besondere an diesen geplanten Fahrten sind abwechslungsreiche Tage. Es finden viele Aktionen statt, beispielsweise ein Geländespiel über den ganzen Tag, verschiedene Workshops und abends Singerunden am Lagerfeuer mit Gitarren und anderen Instrumenten. Nachtgeländespiele und Nachtwanderungen gehören auch manchmal dazu. Das Alter spielt hierbei keine besondere Rolle. Alle werden mit einbezogen und können gleichermaßen mitmachen. Ihr könnt jeden Pfadfinder fragen, ob alt ob jung, Kein Lager gerät in Vergessenheit. Sei es durch ultimative Erlebnisse oder doch einfach nur wegen der Flucht aus dem Alltag.'],
    img: 'https://hratuga.de/static/img/Robert%20(44%20von%20309).4788faf.jpg',
  },
  {
    title: 'Der Weg ist das Ziel',
    text: ['Andere Aktionen sind beispielsweise das gemeinsame Wandern über mehrere Tage, das "Hajken". Das bedeutet mit Kompass und Karte navigieren, auf dem Feuer kochen und in der Wildnis mit einem Zelt übernachten. Dabei entdeckt man manchmal ungeahnte Stärken und Schwächen an sich und erlebt eine Gemeinschaft, die durch Zusammenhalt viel erreichen kann.'],
    img: 'https://hratuga.de/static/img/Robert%20(44%20von%20309).4788faf.jpg',
  },
  {
    title: 'Interessiert?',
    text: ['Das alles ist nur ein kleiner Einblick, was es bedeutet Pfadfinder zu sein und wie viel Spaß es macht! Komm doch einfach mal bei uns vorbei und lerne uns kennen. Das Pfadfinderleben ist keine Sache, die man gut in Worte fassen kann, man muss es erleben und ein Teil werden.'],
    img: 'https://hratuga.de/static/img/Robert%20(44%20von%20309).4788faf.jpg',
  },
];
</script>
