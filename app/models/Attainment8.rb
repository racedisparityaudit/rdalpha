class Attainment8

  def initialize
    @json = JSON.parse(File.read(Rails.root.join("./data/input/tier_4_attainment8.json")))
  end

  def blurb_paragraphs
    @json["description"]
  end

  def context_paragraphs
    @json["context"]
  end

  def analysis_paragraphs
    @json["analysis"]
  end

end
