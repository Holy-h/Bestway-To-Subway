module.exports = {
  purge: [],
  theme: {
    extend: {
      spacing: {
        "72": "18rem",
        "84": "21rem",
      },
      minWidth: {
        "40": "10rem",
      },
    },
  },
  variants: {
    margin: ["responsive", "last"],
    textColor: ["responsive", "hover", "group-hover", "focus"],
  },
  plugins: [],
};
