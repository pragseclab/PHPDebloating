<?php

/* display/export/options_output_separate_files.twig */
class __TwigTemplate_5a1eea3d2652a0fa7e59d2d66540d5e1eb2aedced7f121f1c9996704841b5424 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        echo "<li>
    <input type=\"checkbox\" id=\"checkbox_as_separate_files\"
        name=\"as_separate_files\" value=\"";
        // line 3
        echo twig_escape_filter($this->env, ($context["export_type"] ?? null), "html", null, true);
        echo "\"";
        // line 4
        echo ((($context["is_checked"] ?? null)) ? (" checked") : (""));
        echo ">
    <label for=\"checkbox_as_separate_files\">
        ";
        // line 6
        if ((($context["export_type"] ?? null) == "server")) {
            // line 7
            echo "            ";
            echo _gettext("Export databases as separate files");
            // line 8
            echo "        ";
        } elseif ((($context["export_type"] ?? null) == "database")) {
            // line 9
            echo "            ";
            echo _gettext("Export tables as separate files");
            // line 10
            echo "        ";
        }
        // line 11
        echo "    </label>
</li>
";
    }

    public function getTemplateName()
    {
        return "display/export/options_output_separate_files.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  45 => 11,  42 => 10,  39 => 9,  36 => 8,  33 => 7,  31 => 6,  26 => 4,  23 => 3,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "display/export/options_output_separate_files.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/display/export/options_output_separate_files.twig");
    }
}
